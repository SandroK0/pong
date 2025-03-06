package main

import (
	"fmt"
	"net"
)

var clients = make(map[string]net.Addr) // Stores two client addresses

func main() {
	addr := ":5000"
	conn, err := net.ListenPacket("udp", addr)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer conn.Close()

	fmt.Println("UDP relay started on", addr)

	buffer := make([]byte, 1024)
	for {
		n, clientAddr, err := conn.ReadFrom(buffer)
		if err != nil {
			fmt.Println("Read error:", err)
			continue
		}

		message := string(buffer[:n])
		fmt.Printf("Received from %s: %s\n", clientAddr.String(), message)

		// Store the client if it's new
		if _, exists := clients[clientAddr.String()]; !exists {
			clients[clientAddr.String()] = clientAddr
		}

		// Forward the message to the other client
		for addrStr, addr := range clients {
			if addrStr != clientAddr.String() { // Send to the other client
				_, err := conn.WriteTo([]byte(message), addr)
				if err != nil {
					fmt.Println("Error forwarding message to", addr, ":", err)
				} else {
					fmt.Printf("Forwarded to %s\n", addr.String())
				}
			}
		}
	}
}
