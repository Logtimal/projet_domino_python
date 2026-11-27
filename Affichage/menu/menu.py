import pygame
import sys
from jeuPrincipal.ecranPrincipal import ecran_principal

WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
BG = (60,25,60)

# Textes des boutons du menu, de haut en bas
BOUTONS = [
    "Nouvelle partie avec talon",
    "Nouvelle partie sans talon (sans pioche)",
    "Enregistrer",
    "Importer",
    "Quitter",
]


def start_menu():

    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Domino")

    font = pygame.font.SysFont("Corbel", 32)
    title_font = pygame.font.SysFont("Corbel", 110, bold=True)

    while True:

        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        title_text = title_font.render("Domino", True, WHITE)
        screen.blit(title_text, title_text.get_rect(center=(360, 130)))

        boutons = {}
        for i, texte in enumerate(BOUTONS):
            button = pygame.Rect(60, 260 + i * 80, 600, 55)
            pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button)

            button_text = font.render(texte, True, WHITE)
            screen.blit(button_text, button_text.get_rect(center=button.center))

            boutons[texte] = button

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Les deux boutons "Nouvelle partie" ouvrent l'écran de jeu
                if (boutons["Nouvelle partie avec talon"].collidepoint(event.pos)
                        or boutons["Nouvelle partie sans talon (sans pioche)"].collidepoint(event.pos)):
                    ecran_principal()
                    # De retour au menu, on remet la fenêtre à la taille du menu
                    screen = pygame.display.set_mode((720, 720))

                # "Enregistrer" et "Importer" ne font rien pour l'instant
                if boutons["Quitter"].collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
