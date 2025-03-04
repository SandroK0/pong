from settings import PLAYER_SPEED, SCREEN_HEIGHT
import pygame
from settings import WHITE, SCREEN_WIDTH


class Player:

    def __init__(self, screen) -> None:
        self.screen = screen

    def draw(self):
        pass


class RightPlayer(Player):

    def __init__(self, screen):
        super().__init__(screen)
        self.pos = pygame.Vector2(SCREEN_WIDTH - 40, 300)

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 20, 100)
        pygame.draw.rect(self.screen, WHITE, player, 0)

    def ai_move(self, ball):
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


class LeftPlayer(Player):

    def __init__(self, screen):
        super().__init__(screen)
        self.pos = pygame.Vector2(20, 300)

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 20, 100)
        pygame.draw.rect(self.screen, WHITE, player, 0)
