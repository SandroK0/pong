package main

import (
	"fmt"
	"net"
)

func main() { 
	addr := ":5000"
	conn, err := net.ListenPacket("udp", addr)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer conn.Close()

	fmt.Println("UDP matchmaking server started on", addr)


    buffer := make([]byte, 1024)
    for { 
        n, _, err := conn.ReadFrom(buffer)
        if err != nil { 
            fmt.Println("Read error", err)
            continue
        }

        fmt.Println(string(buffer[:n]))

    }
}
