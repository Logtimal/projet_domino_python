import Domino
import random

# Fonction pour construire une pioche de dominos
def buildPioche():
    pioche = []
    for i in range(0, 7):
        for j in range(i, 7):
            domino = Domino.Domino(i, j)
            pioche.append(domino)
    return pioche

# Fonction pour piocher un domino de façon aléatoire de la pioche
def drawDomino(pioche):
    if len(pioche) == 0:
        return None
    else:
        index = random.randint(0, len(pioche) - 1)
        domino = pioche[index]
        pioche.remove(domino)
        return domino