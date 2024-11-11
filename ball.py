import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED


class Ball:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = pygame.Vector2(7, 0)

    def change_ball_direction(self, player_pos):
        # -50 to center it to the paddle
        diff = (self.pos.y - player_pos.y) - 50
        # Copy the current direction
        new_direction = pygame.Vector2(self.direction)
        new_direction.y = diff / 10  # scale down the difference
        new_direction.x = -new_direction.x  # reverse the x direction

        # Normalize the ball direction to maintain constant speed
        new_direction.normalize_ip()
        new_direction *= BALL_SPEED

        self.direction = new_direction

    def render(self):

        pygame.draw.circle(self.screen, "white", self.pos, 10)

    def reset(self, k):
        self.pos = pygame.Vector2(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.direction = pygame.Vector2(k * 7, 0)

    def update(self):
        self.pos.x += self.direction.x
        self.pos.y += self.direction.y
