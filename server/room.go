package main

import (
	"time"
)

type Manager struct {
	Rooms     map[string]*Room
	ClientMap map[string]string // Maps client address to room ID
}

// Room represents a game room
type Room struct {
	ID        string                `json:"id"`
	Name      string                `json:"name"`
	Players   map[int]*Player       `json:"players"`
	Balls     map[int]*Ball         `json:"balls"`
	Score     int                   `json:"score"`
	CreatedAt time.Time             `json:"created_at"`
	UpdatedAt time.Time             `json:"updated_at"`
	Clients   map[string]ClientInfo `json:"-"` // Not serialized
}

// Player represents a player in a room
type Player struct {
	ID       int     `json:"id"`
	Username string  `json:"username"`
	X        float64 `json:"x"`
	Y        float64 `json:"y"`
}

// Ball represents a ball in the game
type Ball struct {
	ID int     `json:"id"`
	X  float64 `json:"x"`
	Y  float64 `json:"y"`
}

// ClientInfo stores information about a connected client
type ClientInfo struct {
	Address  string
	PlayerID int
	Username string
}
