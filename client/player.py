from settings import PLAYER_SPEED, SCREEN_HEIGHT
import pygame
from settings import WHITE, SCREEN_WIDTH
from ball import Ball

class Player:

    def __init__(self, screen, x_pos) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(x_pos, 300)

    def ai_move(self, ball: Ball):
        # Get paddle center point
        paddle_center = self.pos.y + 50  # Assuming paddle height is 100
        
        # Get target position (ball's center)
        target_y = ball.pos.y
        
        # Calculate distance to target
        distance = target_y - paddle_center
        
        # Use proportional speed (adjust 0.1 coefficient for responsiveness)
        smooth_speed = distance * 0.1
        
        # Limit speed to PLAYER_SPEED
        smooth_speed = max(min(smooth_speed, PLAYER_SPEED), -PLAYER_SPEED)
        
        # Move paddle with bounds checking
        new_y = self.pos.y + smooth_speed
        
        # Keep paddle within screen bounds
        if new_y + 100 > SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT - 100
        elif new_y < 0:
            self.pos.y = 0
        else:
                self.pos.y = new_y

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 20, 100)
        pygame.draw.rect(self.screen, WHITE, player, 0)


class RightPlayer(Player):

    def __init__(self, screen):
        super().__init__(screen, SCREEN_WIDTH - 40)

    

    def handle_press(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.pos.y > 0:
            self.pos.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.pos.y + 100 < SCREEN_HEIGHT:
            self.pos.y += PLAYER_SPEED


class LeftPlayer(Player):

    def __init__(self, screen):
        super().__init__(screen, 20)

    def handle_press(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos.y > 0:
            self.pos.y -= PLAYER_SPEED
        if keys[pygame.K_s] and self.pos.y + 100 < SCREEN_HEIGHT:
            self.pos.y += PLAYER_SPEED
