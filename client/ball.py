import pygame
import json  # Add this import if not already in your file
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED, SERVER_ADDR

class Ball:
    def __init__(self, screen, sock) -> None:
        self.screen = screen
        self.sock = sock  # UDP socket passed from the main script
        self.pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = pygame.Vector2(7, 0)

    def change_ball_direction(self, player_pos):
        # -50 to center it to the paddle
        diff = (self.pos.y - player_pos.y) - 50
        # Copy the current direction
        new_direction = pygame.Vector2(self.direction)
        new_direction.y = diff / 10  # Scale down the difference
        new_direction.x = -new_direction.x  # Reverse the x direction

        # Normalize the ball direction to maintain constant speed
        new_direction.normalize_ip()
        new_direction *= BALL_SPEED

        self.direction = new_direction

    def render(self):
        pygame.draw.circle(self.screen, "white", self.pos, 10)

    def reset(self, k):
        self.pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = pygame.Vector2(k * 7, 0)

    def update(self):
        # Update ball position
        self.pos.x += self.direction.x
        self.pos.y += self.direction.y

        # Prepare ball position data to send
        # ball_data = {
        #     "ball_x": self.pos.x,
        #     "ball_y": self.pos.y
        # }

        # # Convert to JSON and encode to bytes, then send via UDP
        # message = json.dumps(ball_data).encode('utf-8')
        # self.sock.sendto(message, SERVER_ADDR)  # Replace with your server's IP and port