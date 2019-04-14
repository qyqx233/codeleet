package main

import (
	"bufio"
	"fmt"
	"io"
	"net"
	"os"
	"strings"
)

func int2Bytes(n int) []byte {
	x := int32(n)
	return []byte{byte(x >> 24 & 255), byte(x >> 16 & 255), byte(x >> 8 & 255), byte(x >> 0 & 255)}
}

func bytes2Int(b []byte) int {
	return int(int32(b[0])<<24 | int32(b[1])<<16 | int32(b[2])<<8 | int32(b[3]))
}

func call1(filename string, content string) error {
	conn, err := net.Dial("tcp", "localhost:5566")
	var reader io.Reader
	if err != nil {
		return nil
	}
	if filename != "" {
		fd, err := os.Open(filename)
		if err != nil {
			return err
		}
		reader = bufio.NewReader(fd)
	} else {
		reader = strings.NewReader(content)
	}

	n, err := io.Copy(conn, reader)
	fmt.Printf("send %d bytes\n", n)
	buf := make([]byte, 1000)
	conn.Read(buf)
	return nil
}

func writeData(conn net.Conn, data []byte) {
	conn.Write(int2Bytes(len(data)))
	conn.Write(data)
}

func send(filename string) error {
	return nil
}

func call(filename string, content string) error {
	var reader io.Reader
	// var head []byte
	if filename != "" {
		fd, err := os.Open(filename)
		if err != nil {
			return err
		}
		defer fd.Close()
		reader = bufio.NewReader(fd)
	} else {
		reader = strings.NewReader(content)
	}
	conn, err := net.Dial("tcp", "localhost:5566")
	if err != nil {
		return err
	}
	defer conn.Close()
	if filename != "" {
		io.Copy(conn, reader)
	} else {
		conn.Write([]byte("AGREE-TECH-SEND-FILE"))
		writeData(conn, []byte("a.txt"))
		writeData(conn, []byte("fileCheckFlag|false"))
		writeData(conn, []byte("1234"))
	}
	// n, err := io.Copy(conn, reader)
	// fmt.Printf("send %d bytes\n", n)
	buf := make([]byte, 1000)
	// conn.Read(buf)
	n, err := conn.Read(buf)
	if err != nil {
		return err
	}
	fmt.Println(string(buf[:n]))
	return nil
}

func main() {
	err := call("", "AGREE-TECH-RECV-FILE"+strings.Repeat(" ", 95)+"a.txt "+"123")
	if err != nil {
		fmt.Println(err)
	}
	// call("", "AGREE-TECH-RECV-FILE"+strings.Repeat(" ", 95)+"b.txt "+"123")
}
