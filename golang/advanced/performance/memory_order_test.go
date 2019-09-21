package performance 
import(
	"log"
	"runtime"
	"testing"
)

func Test_1(t *testing.T) {
	var a string
	var done bool
	setup := func () {
		a = "hello, world"
		done = true
		if done {
			log.Println(len(a)) // 如果被打印出来，它总是12
		}
	}
	go setup()

	for !done {
		runtime.Gosched()
	}
	log.Println(a) // 期待的打印结果：hello, world
}

func Test_2(t *testing.T) {
	var b bool
	if b {
		t.Log("true")
	} else {
		t.Log("false")
	}
}

func Test_3 (t *testing.T) {
	 f3 := func() {
		var a, b int
		var c = make(chan bool)
	
		go func() {
			a = 1
			c <- true
			if b != 1 {
				panic("b != 1") // 绝不可能发生
			}
		}()
	
		go func() {
			<-c
			b = 1
			if a != 1  {
				panic("a != 1") // 绝不可能发生
			}
		}()
	}
	f3()
}

func Test_4(t *testing.T) {
	var a, b, x, y int
	c := make(chan bool)

	go func() {
		a = 1
		c <- true
		x = 1
	}()

	go func() {
		b = 1
		<-c
		y = 1
	}()

	// 一个和上面的数据通道操作不相关的协程。
	// 这是一个不良代码的例子，它造成了很多数据竞争。
	go func() {
		if x == 1 {
			if a != 1 {
				panic("a != 1") // 有可能发生
			}
			if b != 1 {
				panic("b != 1") // 有可能发生
			}
		}

		if y == 1 {
			if a != 1 {
				panic("a != 1") // 有可能发生
			}
			if b != 1 {
				panic("b != 1") // 有可能发生
			}
		}
	}()
}