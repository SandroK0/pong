import pygame
from menu.menu import Menu
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    STATE = {
        'in_menu': True,
    }

    game = Game(screen)
    menu = Menu(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if STATE['in_menu']:
                menu.handle_events(event, game, STATE)
            else:
                game.handle_events(event, STATE)

        if STATE['in_menu']:
            menu.update()
            menu.render()

        else:
            game.update()
            game.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
