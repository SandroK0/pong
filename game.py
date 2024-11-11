import pygame
from player import LeftPlayer, RightPlayer
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, PLAYER_SPEED, BALL_SPEED
from ball import Ball
from menu.button import Button


class Game:

    def __init__(self, screen) -> None:

        pygame.font.init()

        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.mode = None
        self.player1 = LeftPlayer(screen)
        self.player2 = RightPlayer(screen)
        self.ball = Ball(screen)
        self.player1_score = 0
        self.player2_score = 0
        self.reset_btn = Button((SCREEN_WIDTH / 2) - 200, 20, 200,
                                50, "reset", self.font, (0, 0, 0), (0, 0, 0), WHITE)
        self.menu_btn = Button((SCREEN_WIDTH) / 2 + 20, 20, 200,
                               50, "menu", self.font, (0, 0, 0), (0, 0, 0), WHITE)

    def update(self):

        keys = pygame.key.get_pressed()
        self.handle_press_p1(keys)
        if self.mode == "2p":
            self.handle_press_p2(keys)
        else:
            self.ai_move()
        self.ball.update()
        self.handle_collisions()

    def reset_score(self):
        self.player1_score = 0
        self.player2_score = 0

    def handle_events(self, event, state):
        if self.reset_btn.is_clicked(event):
            self.reset_score()
            self.ball.reset(1)
        if self.menu_btn.is_clicked(event):
            self.reset_score()
            self.ball.reset(1)
            state['in_menu'] = True

    def render(self):

        # Draw background
        self.screen.fill("black")

        self.reset_btn.draw(self.screen)
        self.menu_btn.draw(self.screen)

        pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH / 2, 0, 10, 700), 0)
        self.render_score()

        self.player1.render()
        self.player2.render()
        self.ball.render()

    def render_score(self):
        player1_text = self.font.render(str(self.player1_score), True, WHITE)
        player2_text = self.font.render(str(self.player2_score), True, WHITE)

        self.screen.blit(player1_text, (self.screen.get_width() / 4, 20))
        self.screen.blit(player2_text, (self.screen.get_width() * 3 / 4, 20))

    def handle_press_p1(self, keys):
        if keys[pygame.K_w]:
            if not self.player1.pos.y <= 0:
                self.player1.pos.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            if not self.player1.pos.y + 100 >= SCREEN_HEIGHT:
                self.player1.pos.y += PLAYER_SPEED

    def handle_press_p2(self, keys):
        if keys[pygame.K_UP]:
            if not self.player2.pos.y <= 0:
                self.player2.pos.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            if not self.player2.pos.y + 100 >= SCREEN_HEIGHT:
                self.player2.pos.y += PLAYER_SPEED

    def ai_move(self):

        # AI Xd
        if self.ball.pos.y not in range(int(self.player2.pos.y), int(self.player2.pos.y + 100)) and self.ball.pos.x > 0:
            if self.player2.pos.y + 50 < self.ball.pos.y and not self.player2.pos.y + 100 >= SCREEN_HEIGHT:
                self.player2.pos.y += PLAYER_SPEED
            if self.player2.pos.y + 50 > self.ball.pos.y and not self.player2.pos.y <= 0:
                self.player2.pos.y -= PLAYER_SPEED

    def handle_collisions(self):

        # Collision to top and bottom
        if self.ball.pos.y + 10 >= SCREEN_HEIGHT:
            self.ball.direction.y = -BALL_SPEED
            self.ball.direction.normalize_ip()
            self.ball.direction *= BALL_SPEED

        if self.ball.pos.y - 10 <= 0:
            self.ball.direction.y = BALL_SPEED
            self.ball.direction.normalize_ip()
            self.ball.direction *= BALL_SPEED

        # Collision to right paddle
        if self.ball.pos.x + 10 >= self.player2.pos.x and self.ball.pos.x + 10 <= self.player2.pos.x + 20 and self.ball.pos.y + 10 >= self.player2.pos.y and self.ball.pos.y - 10 <= self.player2.pos.y + 100:
            self.ball.change_ball_direction(
                self.player2.pos)

        # Goal in the right
        if self.ball.pos.x > 1300:
            self.player1_score += 1
            self.ball.reset(1)

        # Collision to left paddle
        if self.ball.pos.x - 10 <= self.player1.pos.x + 20 and self.ball.pos.x - 10 >= self.player1.pos.x and self.ball.pos.y + 10 >= self.player1.pos.y and self.ball.pos.y - 10 <= self.player1.pos.y + 100:
            self.ball.change_ball_direction(
                self.player1.pos)

        # Goal in the left
        if self.ball.pos.x < -20:
            self.player2_score += 1
            self.ball.reset(-1)
