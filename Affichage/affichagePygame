import pygame
import sys
from menu.menu import start_menu

WHITE = (255,255,255)

def game():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont("Corbel", 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((40, 40, 40))

        text = font.render("Game Started!", True, WHITE)
        screen.blit(text, (250, 350))

        pygame.display.update()

start_menu()
