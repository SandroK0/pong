# menu.py
import pygame
from .button import Button
from settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.in_menu = True
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 64)  # Font for the title text
        # Create button and input box instances
        self.one_player = Button((SCREEN_WIDTH - 200) / 2, SCREEN_HEIGHT /
                                 2 - 50, 200, 50, "1 Player", self.font, (0, 0, 0), (0, 0, 0), WHITE)
        self.two_player = Button((SCREEN_WIDTH - 200) / 2, SCREEN_HEIGHT /
                                 2, 200, 50, "2 Player", self.font, (0, 0, 0), (0, 0, 0), WHITE)
        self.play_online = Button((SCREEN_WIDTH - 200) / 2, SCREEN_HEIGHT /
                                  2 + 50, 200, 50, "Play Online", self.font, (0, 0, 0), (0, 0, 0), WHITE)

    def handle_events(self, event, game):
        if self.one_player.is_clicked(event):
            game.mode = "1p"
            self.in_menu = False
        if self.two_player.is_clicked(event):
            game.mode = "2p"
            self.in_menu = False
        if self.play_online.is_clicked(event):
            game.mode = "online"
            self.in_menu = False

    def render(self):
        self.screen.fill("black")

        title_text = self.title_font.render("Welcome to Pong!", True, WHITE)
        # Render the welcome text
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150))

        self.screen.blit(title_text, title_rect)
        # Draw the button and input box
        self.one_player.draw(self.screen)
        self.two_player.draw(self.screen)
        self.play_online.draw(self.screen)
