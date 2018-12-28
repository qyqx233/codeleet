package main

import (
	"fmt"
)

type S struct {
	M *int
}

func ref(y *int, z *S) {
	z.M = y
}

func main() {
	var x S
	var i int
	ref(&i, &x)
	fmt.Println("ok")
}
