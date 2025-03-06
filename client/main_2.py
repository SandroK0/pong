import pygame
from menu.menu import Menu
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CLIENT_PORT
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5002))

# Function to handle UDP listening
def udp_listener(game: Game):
    while True:
        data, addr = sock.recvfrom(1024)
        game.handle_udp_packet(data, addr)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    menu = Menu(screen)
    game = Game(screen, menu, sock, False)

    # Start UDP listening in a separate thread
    threading.Thread(target=udp_listener, args=(game,), daemon=True).start()

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
    sock.close()


if __name__ == "__main__":
    main()
