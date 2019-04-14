package main

import "fmt"

// Set 集合
type Set struct {
	mp map[string]struct{}
}

// Init 初始化
func (set *Set) Init() {
	set.mp = make(map[string]struct{})
	fmt.Printf("mp at %p\n", &(set.mp))
}

// Add 集合新增元素
func (set *Set) Add(e string) bool {
	if _, ok := set.mp[e]; !ok {
		// mp[e] = new(struct{})
		set.mp[e] = struct{}{}
		return true
	}
	return false
}

func main() {
	set := Set{}
	set.Init()
	fmt.Println(set.mp)
	fmt.Println(set.Add("a"))
	fmt.Println(set.Add("a"))
	fmt.Println(set.Add("b"))
}
