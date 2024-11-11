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


class LeftPlayer(Player):

    def __init__(self, screen):
        super().__init__(screen)
        self.pos = pygame.Vector2(20, 300)

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 20, 100)
        pygame.draw.rect(self.screen, WHITE, player, 0)
