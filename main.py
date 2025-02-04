import pygame

from constants import *


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Window")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((0, 128, 255))

    pygame.display.flip()


def main():
    init_screen()


if __name__ == "__main__":
    main()
