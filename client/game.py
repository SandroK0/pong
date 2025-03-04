from settings import SCREEN_HEIGHT, BALL_SPEED
import pygame
from player import LeftPlayer, RightPlayer
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, PLAYER_SPEED, BALL_SPEED, SERVER_ADDR
from ball import Ball
from menu.button import Button
import socket
import json


class Game:
    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu
        self.mode = None  # "1p", "2p", "online"
        self.font = pygame.font.Font(None, 74)

        self.player1 = LeftPlayer(screen)
        self.player2 = RightPlayer(screen)
        self.ball = Ball(screen)
        self.collision_handler = CollisionHandler(self.ball, self.player1, self.player2)

        self.player1_score = 0
        self.player2_score = 0

        self.reset_btn = Button(SCREEN_WIDTH / 2 - 200, 20, 200, 50, "reset",
                                self.font, (0, 0, 0), (0, 0, 0), WHITE)
        self.menu_btn = Button(SCREEN_WIDTH / 2 + 20, 20, 200, 50, "menu",
                               self.font, (0, 0, 0), (0, 0, 0), WHITE)

    def update(self):
        if self.mode == "1p":
            self.handle_press_p1()
            self.player2.ai_move(self.ball)
        elif self.mode == "2p":
            self.handle_press_p1()
            self.handle_press_p2()

        self.ball.update()
        self.collision_handler.check_collisions()
        self.check_goal()

    def handle_events(self, event):
        if self.reset_btn.is_clicked(event):
            self.reset_game()
        if self.menu_btn.is_clicked(event):
            self.reset_game()
            self.menu.in_menu = True

    def render(self):
        self.screen.fill("black")
        self.reset_btn.draw(self.screen)
        self.menu_btn.draw(self.screen)
        pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH / 2, 0, 10, SCREEN_HEIGHT), 0)

        self.render_score()
        self.player1.render()
        self.player2.render()
        self.ball.render()

    def render_score(self):
        player1_text = self.font.render(str(self.player1_score), True, WHITE)
        player2_text = self.font.render(str(self.player2_score), True, WHITE)
        self.screen.blit(player1_text, (self.screen.get_width() / 4, 20))
        self.screen.blit(player2_text, (self.screen.get_width() * 3 / 4, 20))

    def reset_game(self):
        self.player1_score = 0
        self.player2_score = 0
        self.ball.reset(1)

    def check_goal(self):
        if self.ball.pos.x > SCREEN_WIDTH:
            self.player1_score += 1
            self.ball.reset(1)
        if self.ball.pos.x < -20:
            self.player2_score += 1
            self.ball.reset(-1)

    def handle_press_p1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.player1.pos.y > 0:
            self.player1.pos.y -= PLAYER_SPEED
        if keys[pygame.K_s] and self.player1.pos.y + 100 < SCREEN_HEIGHT:
            self.player1.pos.y += PLAYER_SPEED

    def handle_press_p2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.player2.pos.y > 0:
            self.player2.pos.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.player2.pos.y + 100 < SCREEN_HEIGHT:
            self.player2.pos.y += PLAYER_SPEED


class CollisionHandler:
    def __init__(self, ball, player1, player2):
        self.ball = ball
        self.player1 = player1
        self.player2 = player2

    def check_collisions(self):
        # Top/Bottom Wall Collision
        if self.ball.pos.y + 10 >= SCREEN_HEIGHT or self.ball.pos.y - 10 <= 0:
            self.ball.direction.y *= -1

        # Left Paddle Collision
        if self.ball.pos.x - 10 <= self.player1.pos.x + 20 and self.player1.pos.y <= self.ball.pos.y <= self.player1.pos.y + 100:
            self.ball.change_ball_direction(self.player1.pos)

        # Right Paddle Collision
        if self.ball.pos.x + 10 >= self.player2.pos.x and self.player2.pos.y <= self.ball.pos.y <= self.player2.pos.y + 100:
            self.ball.change_ball_direction(self.player2.pos)
