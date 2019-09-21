package lang

import (
	"testing"
	"fmt"
	"math/rand"
	"runtime"
	"time"
)

func longTimeRequest() <-chan int32 {
	r := make(chan int32)

	go func() {
		time.Sleep(time.Second * 3) // 模拟一个工作负载
		r <- rand.Int31n(100)
	}()

	return r
}

func sumSquares(a, b int32) int32 {
	return a*a + b*b
}

func Test_chanFunc(t *testing.T) {
	chanFunc := func(ch chan <-int) {
		ch <- rand.Int()
		close(ch)
	}
	ch := make(chan int, 0)
	go chanFunc(ch)
	t.Log(<-ch)
}

func Test_chanFunc1(t *testing.T) {
	chanFunc := func(ch <-chan int) {
		t.Log(<-ch)
	}
	ch := make(chan int, 0)
	go chanFunc(ch)
	runtime.Gosched()
	close(ch)
}


func Test_AA(t *testing.T) {
	rand.Seed(time.Now().UnixNano())

	a, b := longTimeRequest(), longTimeRequest()
	fmt.Println(sumSquares(<-a, <-b))
}
