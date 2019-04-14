package main

import "fmt"

func testMake() {
	slice := make([]int, 10)
	fmt.Println(slice)
	mp := make(map[string]int)
	_, ok := mp["a"]
	if ok {
		fmt.Println("has a")
	} else {
		fmt.Println("has no a")
	}
	fmt.Println(mp)
}

func testNew() {
	mp := new(map[string]int)
	_, ok := (*mp)["a"]
	if ok {
		fmt.Println("has a")
	} else {
		fmt.Println("has no a")
	}
}

func main() {
	testNew()
	testMake()
}
