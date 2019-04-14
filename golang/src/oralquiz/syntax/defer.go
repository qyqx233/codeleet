package main

import (
	"encoding/json"
	"fmt"
	"runtime"
	"sync"
	"time"
)

func main() {
	// deferCall()
	// travelStudents()
	// waitGroup()
	// mapTest()
	// jsonTest()
	// chanTest()
	// mapTest1()
	// funcTest()
	// argfuncTest("a", "b", "c")
	// structTest()
	// t := teacherShow{}
	// t.peopleShow.showA()
	// t.showB()
	// foo()
	selectTest()
}

type Student struct {
	Name string
	Age  int
}

// go的闭包
func waitGroup() {
	runtime.GOMAXPROCS(1)
	wg := sync.WaitGroup{}
	wg.Add(20)
	for i := 0; i < 10; i++ {
		go func() {
			fmt.Println("A: ", i) // 此处i是循环退出后的值
			wg.Done()
		}()
	}
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Println("B: ", i)
			wg.Done()
		}(i)
	}
	wg.Wait()
}

func travelStudents() {
	m := make(map[string]*Student)
	stus := []Student{
		{Name: "Jack", Age: 10},
		{Name: "Helen", Age: 20},
	}
	for _, stu := range stus {
		m[stu.Name] = &stu
	}
	fmt.Println(m)
}

// panic在所有的defer执行后才会调用
func deferCall() {
	defer func() { fmt.Println("print before") }()
	panic("panic")
	defer func() { fmt.Println("print doing") }()
	defer func() { fmt.Println("print after") }()
	print("aha\n")
	// panic("panic")
}

func mapTest() {
	type Param map[string]interface{}
	type Show struct {
		Param
	}
	s := new(Show)
	s.Param["RMB"] = 1000
}

func reflectTest() {
	type Student struct {
		Name string
	}
	func(v interface{}) {
		// switch msg := v.(type) {
		// case *Student, Student:
		// fmt.Println(msg.Name)
		// msg.Name
		// }
	}(Student{})
}

// json结构体字段名必须首字母大写
func jsonTest() {
	type People struct {
		Name string `json:"name"`
	}
	js := `{
			"name": "11"
		}`
	var p People
	err := json.Unmarshal([]byte(js), &p)
	if err != nil {
		fmt.Println("err: ", err)
		return
	}
	fmt.Println("people: ", p)
	fmt.Println("people: ", p.Name)
}

// chan必须关闭，一般由生产者关闭，消费者获取后必须判断返回值
func chanTest() {
	abc := make(chan int, 1)
	go func() {
		for i := 0; i < 10; i++ {
			abc <- 1
		}
		close(abc)
	}()
	go func() {
		for {
			a, ok := <-abc
			if !ok {
				return
			}
			fmt.Println("a: ", a)
		}
	}()
	fmt.Println("close")
	time.Sleep(time.Second * 2)
}

// 如果map的val是个结构体
func mapTest1() {
	type Student struct {
		name string
	}
	m := map[string]Student{"people": {"jack"}}
	fmt.Println(m["people"])
	fmt.Println(m["abc"].name)
	a, ok := m["abc"]
	if !ok {
		fmt.Println("no key")
	} else {
		fmt.Println(a)
	}
	fmt.Println(m)
	m1 := map[string]string{"a": "a"}
	fmt.Println(m1["b"])
}

func funcTest() {
	type query func(string) string
	exec := func(name string, vs ...query) string {
		ch := make(chan string)
		fn := func(i int) {
			ch <- vs[i](name)
		}
		for i := range vs {
			go fn(i)
		}
		// close(ch)
		return <-ch
	}
	ret := exec("111", func(n string) string {
		return n + "func1"
	}, func(n string) string {
		return n + "func2"
	})
	fmt.Println(ret)
}

func argfuncTest(vs ...string) {
	for i := range vs {
		fmt.Println(i, vs[i])
	}
}

type People struct {
	Name string
}

// String 方法在sprintf时调用
func (p *People) String() string {
	fmt.Println("call String method")
	// return fmt.Sprintf("print:", p)
	return ""
}
func structTest() {
	p := &People{}
	fmt.Println(p)
}

type peopleShow struct{}

func (p *peopleShow) showA() {
	fmt.Println("showA")
	p.showB()
}

func (p *peopleShow) showB() {
	fmt.Println("showB")
}

type teacherShow struct {
	peopleShow
}

func (t *teacherShow) showB() {
	fmt.Println("teacher showb")
}

type People1 interface {
	Show()
}

type Student1 struct{}

func (stu *Student1) Show() {

}

func live() People1 {
	var stu *Student1
	return stu
}

func foo() {
	if t := live(); t == nil {
		fmt.Println("AAAA")
	} else {
		fmt.Println("BBB ", &t)
	}

}

func selectTest() {
	runtime.GOMAXPROCS(1)
	intChan := make(chan int, 10)
	strChan := make(chan string, 10)
	intChan <- 1
	strChan <- ""
	select {
	case val := <-intChan:
		fmt.Println("got int", val)
	case val := <-strChan:
		fmt.Println("got string", val)
		panic("oh no")
	}
}
