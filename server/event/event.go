package event

// Event is an interface for all event types
type Event interface {
	GetType() string
}

// BaseEvent represents the base structure of all events
type BaseEvent struct {
	Type string `json:"type"`
}

func (e BaseEvent) GetType() string {
	return e.Type
}

// JoinEvent represents a join event
type JoinEvent struct {
	BaseEvent
	RoomID string `json:"room_id"`
}

// LeftEvent represents a left event
type LeftEvent struct {
	BaseEvent
	User     string `json:"user"`
	RoomID   string `json:"room_id"`
	PlayerID int    `json:"player_id"`
}

// UpdateBallEvent represents an update ball event
type UpdateBallEvent struct {
	BaseEvent
	RoomID string  `json:"room_id"`
	BallID int     `json:"ball_id"`
	X      float64 `json:"x"`
	Y      float64 `json:"y"`
}

// UpdatePlayerPosEvent represents an update player position event
type UpdatePlayerPosEvent struct {
	BaseEvent
	RoomID string  `json:"room_id"`
	Player string  `json:"player"`
	X      float64 `json:"x"`
	Y      float64 `json:"y"`
}

// UpdateScoreEvent represents an update score event
type UpdateScoreEvent struct {
	BaseEvent
	RoomID string `json:"room_id"`
	Score  int    `json:"score"`
}

// CreateRoomEvent represents a request to create a new room
type CreateRoomEvent struct {
	BaseEvent
	RoomName string `json:"room_name"`
	User     string `json:"user"`
}

// RoomListEvent represents a request to list available rooms
type RoomListEvent struct {
	BaseEvent
}

// RoomListResponseEvent is sent in response to a RoomListEvent
type RoomListResponseEvent struct {
	BaseEvent
	Rooms []RoomInfo `json:"rooms"`
}

// RoomInfo contains basic information about a room
type RoomInfo struct {
	ID          string `json:"id"`
	Name        string `json:"name"`
	PlayerCount int    `json:"player_count"`
}
