package main

import (
	"bytes"
	"encoding/binary"
	"flag"
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"path"
	"time"
)

type configStru struct {
	port      int
	storePath string
}

type ErrorCodeEnum int

//数据包的类型
const (
	OnceReadBytes = 40960
	NoError       = iota
	ProtolError
	UnExceptError
	BrokenPipeError
)

var (
	server = "127.0.0.1:8080"
	config = configStru{}
)

//Packet 这里是包的结构体，其实是可以不需要的
type Packet struct {
	PacketType    byte
	PacketContent []byte
}

//HeartPacket 心跳包，这里用了json来序列化，也可以用github上的gogo/protobuf包
type HeartPacket struct {
	Version   string `json:"version"`
	Timestamp int64  `json:"timestamp"`
}

//ReportPacket 正式上传的数据包
type ReportPacket struct {
	Content   string `json:"content"`
	Rand      int    `json:"rand"`
	Timestamp int64  `json:"timestamp"`
}

//TCPServer 与服务器相关的资源都放在这里面
type TCPServer struct {
	listener   *net.TCPListener
	hawkServer *net.TCPAddr
}

func main() {
	//类似于初始化套接字，绑定端口
	fmt.Println(ProtolError)
	flag.IntVar(&config.port, "port", 8085, "listening port")
	flag.StringVar(&config.storePath, "path", "./upload", "saving path")
	flag.Parse()
	fmt.Printf("listening on port %d\n", config.port)
	fmt.Println("store path " + config.storePath)
	_, cwd := os.Getwd()
	fmt.Printf("current working path %s\n", cwd)
	hawkServer, err := net.ResolveTCPAddr("tcp", fmt.Sprintf(":%d", config.port))
	checkErr(err)
	//侦听
	listen, err := net.ListenTCP("tcp", hawkServer)
	checkErr(err)
	//记得关闭
	defer listen.Close()
	TCPServer := &TCPServer{
		listener:   listen,
		hawkServer: hawkServer,
	}
	fmt.Println("start server successful......")
	//开始接收请求
	for {
		conn, err := TCPServer.listener.Accept()
		fmt.Printf("accept tcp client %s\n", conn.RemoteAddr().String())
		if err != nil {
			fmt.Println(err)
			continue
		}
		// 每次建立一个连接就放到单独的协程内做处理
		go handle(conn)
	}
}

func readNBites(reader io.Reader, bs []byte) (int, error) {
	leng := len(bs)
	var nRead = 0
	for {
		if nRead == leng {
			break
		}
		n, err := reader.Read(bs[nRead:])
		if err != nil {
			if err == io.EOF {
				return nRead, nil
			}
			return 0, err
		}
		nRead += n
	}
	return nRead, nil
}

func int2Bytes(n int) []byte {
	x := int32(n)
	bytesBuffer := bytes.NewBuffer([]byte{})
	binary.Write(bytesBuffer, binary.BigEndian, x)
	return bytesBuffer.Bytes()
}

func int2Bytes1(n int) []byte {
	x := int32(n)
	return []byte{byte(x >> 24 & 255), byte(x >> 16 & 255), byte(x >> 8 & 255), byte(x >> 0 & 255)}
}

func bytes2Int(b []byte) int {
	var x int32
	bytesBuffer := bytes.NewBuffer(b)
	binary.Read(bytesBuffer, binary.BigEndian, &x)
	return int(x)
}

func bytes2Int1(b []byte) int {
	return int(int32(b[0])<<24 | int32(b[1])<<16 | int32(b[2])<<8 | int32(b[3]))
}

func packResponse(conn net.Conn, errorCode int) {
	bs := []byte{byte(errorCode)}
	conn.Write(bs)
}

//handle 处理函数，这是一个状态机
//根据数据包来做解析
//数据包的格式为|0xFF|0xFF|len(高)|len(低)|Data|CRC高16位|0xFF|0xFE
//其中len为data的长度，实际长度为len(高)*256+len(低)
//CRC为32位CRC，取了最高16位共2Bytes
//0xFF|0xFF和0xFF|0xFE类似于前导码
func handle(conn net.Conn) {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println(err)
		}
	}()
	defer conn.Close()
	var t1 = time.Now()
	var err error
	var wn, totalWn int
	var head = make([]byte, 2)
	var lenBytes = make([]byte, 4)
	nRead := 0
	// reader := bufio.NewReader(conn)
	reader := conn
	_, err = reader.Read(head)
	if err != nil {
		packResponse(conn, UnExceptError)
		return
	}
	if head[0] != 88 {
		packResponse(conn, ProtolError)
		return
	}
	var fileNameBytes = make([]byte, int(head[1]))
	_, err = readNBites(reader, fileNameBytes)
	if err != nil {
		packResponse(conn, BrokenPipeError)
		return
	}
	_, err = readNBites(reader, lenBytes)
	if err != nil {
		packResponse(conn, BrokenPipeError)
		return
	}
	fileLen := bytes2Int1(lenBytes)
	log.Printf("filename=%s, len=%d", path.Join(config.storePath, string(fileNameBytes)), fileLen)
	fd, err := os.OpenFile(path.Join(config.storePath, string(fileNameBytes)), os.O_WRONLY|os.O_CREATE, 0644)
	defer fd.Close()
	var buf = make([]byte, OnceReadBytes)
	// var wn int
	for {
		if nRead == fileLen {
			break
		}
		n, err := readNBites(reader, buf)
		if err != nil {
			packResponse(conn, BrokenPipeError)
			return
		}
		// log.Printf("read %d bytes", n)
		if n == OnceReadBytes {
			wn, err = fd.Write(buf)
		} else {
			wn, err = fd.Write(buf[:n])
		}
		if err != nil {
			log.Println(err)
			packResponse(conn, BrokenPipeError)
			return
		}
		totalWn += wn
		nRead += n
	}
	var t2 = time.Now()
	fmt.Printf("write %d %d bytes, cost %d seconds\n", nRead, totalWn, (t2.UnixNano()-t1.UnixNano())/1e9)
	packResponse(conn, NoError)
}

//在这里处理收到的包，就和一般的逻辑一样了，根据类型进行不同的处理，因人而异
//我这里处理了心跳和一个上报数据包
//服务器往客户端的数据包很简单地以\n换行结束了，偷了一个懒:)，正常情况下也可根据自己的协议来封装好
//然后在客户端写一个状态来处理
// func processRecvData(packet *Packet, conn net.Conn) {
//  switch packet.PacketType {
//  case HEART_BEAT_PACKET:
//      var beatPacket HeartPacket
//      json.Unmarshal(packet.PacketContent, &beatPacket)
//      fmt.Printf("recieve heat beat from [%s] ,data is [%v]\n", conn.RemoteAddr().String(), beatPacket)
//      conn.Write([]byte("heartBeat\n"))
//      return
//  case REPORT_PACKET:
//      var reportPacket ReportPacket
//      json.Unmarshal(packet.PacketContent, &reportPacket)
//      fmt.Printf("recieve report data from [%s] ,data is [%v]\n", conn.RemoteAddr().String(), reportPacket)
//      conn.Write([]byte("Report data has recive\n"))
//      return
//  }
// }

//处理错误，根据实际情况选择这样处理，还是在函数调之后不同的地方不同处理
func checkErr(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
