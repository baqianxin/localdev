package main

import "fmt"

// 验证 引用传递  值传递
func main() {
	a := 22
	b := &a
	c := &b
	println(a, &a, b, &b, c, &c)
	test(b)
	c = &b
	test3(b)
	c = &b
	test2(*b)
	println(a, &a, *b, &b, **c, &c)
	persons := make(map[string]int)
	persons["张三"] = 19

	mp := &persons

	fmt.Printf("原始map的内存地址是：%p\n", mp)
	modify(persons)
	fmt.Println("map值被修改了，新值为:", persons)
}

func modify(p map[string]int) {
	fmt.Printf("函数里接收到map的内存地址是：%p\n", &p)
	p["张三"] = 20
}

func test(p *int) {
	*p += 1
	println(p, *p)
}

func test2(v int) {
	v += 1000
	println(&v, v)
}

func test3(p *int) {
	n := *p + 2000
	p = &n
	println(p, *p)
}

//
