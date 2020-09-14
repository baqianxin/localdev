package main

import (
	"fmt"
	"net"
	"time"
)

// socket 编程
func connHandler(c net.Conn) {
	buf := make([]byte, 1024)
	defer c.Close()
	cnt, _ := c.Read(buf)
	c.Write(buf[0:cnt])
}

func main() {
	server, _ := net.Listen("tcp", ":1208")

	fmt.Println("Server started ...", time.Now().Format("2006-01-02 15:04:05 -0700 MST"))

	for {
		conn, _ := server.Accept()
		go connHandler(conn)
	}
}
