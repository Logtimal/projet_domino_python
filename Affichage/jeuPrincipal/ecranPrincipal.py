import os
import pygame
import sys

LARGEUR = 1252
HAUTEUR = 730

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT = (170,170,170)
DARK = (100,100,100)
GRIS_BULLE = (217,217,217)

IMAGE_FOND = os.path.join(os.path.dirname(__file__), "..", "assets", "image_fond.jpg")

# Position du bouton flèche, de la bulle et de ses deux boutons
BOUTON_FLECHE = pygame.Rect(20, 20, 70, 50)
BULLE = pygame.Rect(110, 15, 500, 70)
BOUTON_ENREGISTRER = pygame.Rect(125, 27, 170, 46)
BOUTON_QUITTER = pygame.Rect(310, 27, 285, 46)


# Dessine le bouton flèche : vers la droite si la bulle est fermée, vers la gauche si elle est ouverte
def dessiner_fleche(screen, bulle_ouverte, mouse):

    pygame.draw.rect(screen, LIGHT if BOUTON_FLECHE.collidepoint(mouse) else WHITE, BOUTON_FLECHE, border_radius=8)

    gauche = (BOUTON_FLECHE.left + 15, BOUTON_FLECHE.centery)
    droite = (BOUTON_FLECHE.right - 15, BOUTON_FLECHE.centery)

    if bulle_ouverte:
        pointe, direction = gauche, 1
    else:
        pointe, direction = droite, -1

    x = pointe[0] + direction * 12
    pygame.draw.line(screen, BLACK, gauche, droite, 4)
    pygame.draw.lines(screen, BLACK, False, [(x, pointe[1] - 11), pointe, (x, pointe[1] + 11)], 4)


# Dessine la bulle avec les boutons "Enregistrer" et "Quitter sans enregistrer"
def dessiner_bulle(screen, font, mouse):

    pygame.draw.rect(screen, GRIS_BULLE, BULLE, border_radius=8)

    for button, texte in ((BOUTON_ENREGISTRER, "Enregistrer"), (BOUTON_QUITTER, "Quitter sans enregistrer")):
        pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button, border_radius=6)

        button_text = font.render(texte, True, WHITE)
        screen.blit(button_text, button_text.get_rect(center=button.center))


# Affiche l'écran de jeu, la fonction se termine quand on retourne au menu
def ecran_principal():

    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

    fond = pygame.image.load(IMAGE_FOND).convert()
    fond = pygame.transform.smoothscale(fond, (LARGEUR, HAUTEUR))

    font = pygame.font.SysFont("Corbel", 28)
    bulle_ouverte = False

    while True:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if BOUTON_FLECHE.collidepoint(event.pos):
                    bulle_ouverte = not bulle_ouverte

                elif bulle_ouverte and BOUTON_ENREGISTRER.collidepoint(event.pos):
                    # TODO : sauvegarder la partie avant de retourner au menu
                    return

                elif bulle_ouverte and BOUTON_QUITTER.collidepoint(event.pos):
                    return

        screen.blit(fond, (0, 0))
        dessiner_fleche(screen, bulle_ouverte, mouse)

        if bulle_ouverte:
            dessiner_bulle(screen, font, mouse)

        pygame.display.update()
