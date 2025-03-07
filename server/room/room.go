package room

import (
	"fmt"
	"net"
)

type Manager struct {
	Rooms map[string]*Room
}

type Room struct {
	ID          string  `json:"id"`
	LeftPlayer  *Player `json:"left_player"`
	RightPlayer *Player `json:"right_player"`
	Ball        *Ball   `json:"ball"`
	State       string  `json:"-"` // paused, on, waiting
}

func NewRoom(id string) *Room {
	return &Room{
		ID:   id,
		Ball: new(Ball),
	}
}

type Player struct {
	ClientAddr net.Addr `json:"client_addr"`
	Score      int      `json:"score"` // Moved from Room
	X          float64  `json:"x"`
	Y          float64  `json:"y"`
}

type Ball struct {
	X float64 `json:"x"`
	Y float64 `json:"y"`
}

func NewManager() *Manager {
	return &Manager{
		Rooms: make(map[string]*Room),
	}
}

func (m *Manager) AddPlayer(roomID string, player *Player) error {
	room, exists := m.Rooms[roomID]
	if !exists {

		room = NewRoom(roomID)
		room.LeftPlayer = player
		room.State = "waiting"
		m.Rooms[roomID] = room
		fmt.Println("Room created, Left Player joined")
		return nil
	}

	room.RightPlayer = player
	room.State = "on"

	fmt.Println("Right Player joined")

	return nil
}

// RemovePlayer removes a player from a room
func (m *Manager) RemovePlayer(roomID string, playerID int) error {
	_, exists := m.Rooms[roomID]
	if !exists {
		return fmt.Errorf("room %s not found", roomID)
	}

	return nil
}
