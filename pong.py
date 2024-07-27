import pygame
from math import sqrt, pow

PLAYER_SPEED = 10
BALL_SPEED = 15
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 74)

white = (255, 255, 255)

player1_pos = pygame.Vector2(20, 300)
player2_pos = pygame.Vector2(SCREEN_WIDTH - 40, 300)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_direction = pygame.Vector2(7, 0)

player1_score = 0
player2_score = 0


def calculate_ball_direction(ball: pygame.Vector2, player: pygame.Vector2, current_direction: pygame.Vector2):
    diff = (ball.y - player.y) - 50  # -50 to center it to the paddle
    # Copy the current direction
    new_direction = pygame.Vector2(current_direction)
    new_direction.y = diff / 10  # scale down the difference
    new_direction.x = -new_direction.x  # reverse the x direction

    # Normalize the ball direction to maintain constant speed
    new_direction.normalize_ip()
    new_direction *= BALL_SPEED

    return new_direction



while running:
    player1 = pygame.Rect(player1_pos.x, player1_pos.y, 20, 100)
    player2 = pygame.Rect(player2_pos.x, player2_pos.y, 20, 100)


    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.rect(screen, white, (screen.get_width() / 2, 0, 10, 700), 0)


    pygame.draw.rect(screen, white, player1, 0)
    pygame.draw.rect(screen, white, player2, 0)

    ball = pygame.draw.circle(screen, "white", ball_pos, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not player1_pos.y <= 0:
            player1_pos.y -= PLAYER_SPEED
    if keys[pygame.K_s]:
        if not player1_pos.y + 100 >= SCREEN_HEIGHT:
            player1_pos.y += PLAYER_SPEED
    # if keys[pygame.K_UP]:
    #     if not player2_pos.y <= 0:
    #         player2_pos.y -= PLAYER_SPEED
    # if keys[pygame.K_DOWN]:
    #     if not player2_pos.y + 100 >= SCREEN_HEIGHT:
    #         player2_pos.y += PLAYER_SPEED



    if ball_pos.y + 10 >= SCREEN_HEIGHT:
        ball_direction.y = -BALL_SPEED
        ball_direction.normalize_ip()
        ball_direction *= BALL_SPEED

    if ball_pos.y - 10 <= 0:
        ball_direction.y = BALL_SPEED
        ball_direction.normalize_ip()
        ball_direction *= BALL_SPEED

    if ball_pos.x + 10 >= player2_pos.x and ball_pos.x + 10 <= player2_pos.x + 20 and ball_pos.y + 10 >= player2_pos.y and ball_pos.y - 10 <= player2_pos.y + 100:
        ball_direction = calculate_ball_direction(
            ball_pos, player2_pos, ball_direction)
    if ball_pos.x > 1300:
        player1_score += 1
        ball_pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)
        ball_direction = pygame.Vector2(-7, 0)

    if ball_pos.x - 10 <= player1_pos.x + 20 and ball_pos.x - 10 >= player1_pos.x and ball_pos.y + 10 >= player1_pos.y and ball_pos.y - 10 <= player1_pos.y + 100:
        ball_direction = calculate_ball_direction(
            ball_pos, player1_pos, ball_direction)

    if ball_pos.x < -20:
        player2_score += 1
        ball_pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)
        ball_direction = pygame.Vector2(7, 0)





    # Render the scores
    player1_text = font.render(str(player1_score), True, white)
    player2_text = font.render(str(player2_score), True, white)

    # Position the scores on the screen
    screen.blit(player1_text, (screen.get_width() / 4, 20))
    screen.blit(player2_text, (screen.get_width() * 3 / 4, 20))

    ball_pos.x += ball_direction.x
    ball_pos.y += ball_direction.y

    #AI Xd
    if ball_pos.y not in range(int(player2_pos.y), int(player2_pos.y + 100))  and ball_direction.x > 0:
        if player2_pos.y + 50 < ball_pos.y and not player2_pos.y + 100 >= SCREEN_HEIGHT:
            player2_pos.y += PLAYER_SPEED
        if player2_pos.y + 50 > ball_pos.y and not player2_pos.y <= 0:
            player2_pos.y -= PLAYER_SPEED


    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
