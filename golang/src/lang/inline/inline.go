package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	x := 40
	y := 2
	res := add(x, y)
	fmt.Println(res)
}
