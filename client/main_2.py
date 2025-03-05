import pygame
from menu.menu import Menu
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CLIENT_PORT
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5002))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    menu = Menu(screen)
    game = Game(screen, menu)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if menu.in_menu:
                menu.handle_events(event, game)
            else:
                game.handle_events(event)

        if menu.in_menu:
            menu.render()
        else:
            game.update()
            game.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
