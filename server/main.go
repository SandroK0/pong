package main

import (
	"encoding/json"
	"fmt"
	"gameserver/event"
	"gameserver/room"
	"net"
)

var manager = room.NewManager()

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
		n, ClientAddr, err := conn.ReadFrom(buffer)
		if err != nil {
			fmt.Println("Read error:", err)
			continue
		}

		fmt.Println(string(buffer[:n]))

		var baseEvent event.BaseEvent
		err = json.Unmarshal([]byte(buffer[:n]), &baseEvent)
		if err != nil {
			fmt.Println("Error unmarshalling base event:", err)
		}

		switch baseEvent.GetType() {
		case "join":
			var joinEvent event.JoinEvent

			err := json.Unmarshal([]byte(buffer[:n]), &joinEvent)
			if err != nil {
				fmt.Println("Error unmarshalling join event:", err)
			}

			player := new(room.Player)
			player.ClientAddr = ClientAddr

			manager.AddPlayer(joinEvent.RoomID, player)

		case "updatePlayerPos":
			var UpdatePlayerPosEvent event.UpdatePlayerPosEvent

			err := json.Unmarshal([]byte(buffer[:n]), &UpdatePlayerPosEvent)
			if err != nil {
				fmt.Println("Error unmarshalling join event:", err)
			}

			room, exists := manager.Rooms[UpdatePlayerPosEvent.RoomID]
			if !exists {
				fmt.Println("room not found:", UpdatePlayerPosEvent.RoomID)
			}

			if UpdatePlayerPosEvent.Player == "right_player" {

				_, err := conn.WriteTo([]byte(buffer[:n]), room.LeftPlayer.ClientAddr)
				if err != nil {
					fmt.Println("Error forwarding message to", addr, ":", err)
				}

			} else if UpdatePlayerPosEvent.Player == "left_player" {
				_, err := conn.WriteTo([]byte(buffer[:n]), room.RightPlayer.ClientAddr)
				if err != nil {
					fmt.Println("Error forwarding message to", addr, ":", err)
				}
			}

		}

	}
}
