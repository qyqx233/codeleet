package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

func search(pattern, path string) {
	fd, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	dir := ""
	br := bufio.NewReader(fd)
	n := 0
	for {
		if n == 100 {
			break
		}
		a, _, c := br.ReadLine()
		if c == io.EOF {
			break
		}
		if len(a) == 0 {
			continue
		}
		if a[0] != '\t' {
			dir = string(a)
			continue
		}
		r := strings.Index(string(a), pattern)
		if r >= 0 {
			fmt.Println(dir)
		}
	}
}

func walkDirs(dirs ...string) {
	for _, d := range dirs {
		filepath.Walk(d, func(path string, info os.FileInfo, err error) error {
			// if err != nil {
			// 	return nil
			// }
			if err != nil {
				return nil
			}
			if info.IsDir() {
				fmt.Printf("%s\n", path)
			} else {
				fmt.Printf("\t%s\n", info.Name())
			}
			return nil
		})
	}
}

func main() {
	// walkDirs("c:\\", "d:\\", "e:\\", "f:\\")
	cmd := ""
	if len(os.Args) > 1 {
		cmd = os.Args[1]
	} else {
		cmd = "help"
	}
	if strings.Compare(cmd, "list") == 0 {
		pathes := os.Args[2]
		pathLst := strings.Split(pathes, ",")
		// walkDirs("F:\\英雄时刻")
		fmt.Println(pathLst)
		walkDirs(pathLst...)
	} else if strings.Compare(cmd, "search") == 0 {
		path := os.Args[3]
		pattern := os.Args[2]
		// search("python27.dll", "E:\\Develop\\codeleet\\golang\\src\\tool\\file\\files.txt")
		search(pattern, path)
	} else {
		fmt.Println("listfile.exe search python.dll file.txt")
		fmt.Println("listfile.exe list c:\\\\,b:\\\\")
	}
}
