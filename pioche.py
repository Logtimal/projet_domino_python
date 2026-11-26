import Domino

# Fonction pour construire une pioche de dominos
def buildPioche():
    pioche = []
    for i in range(0, 7):
        for j in range(i, 7):
            domino = Domino.Domino(i, j)
            pioche.append(domino)
    return pioche