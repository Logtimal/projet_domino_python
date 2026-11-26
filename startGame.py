import pioche
import random
def startGame():
    print("Combien de joueurs vont jouer ? (1 - 4)")
    nb_joueurs = int(input())
    return nb_joueurs

def prepareGame(nb_joueurs):
    piocheGlob = pioche.buildPioche()
    joueurs = []
    for i in range(nb_joueurs):
        joueurs.append([i + 1])
        for j in range(7):
            nub = random.randint(0, len(piocheGlob) - 1)
            piece = piocheGlob[nub]
            joueurs[i].append(piece)
            piocheGlob.remove(piece)
    return joueurs, piocheGlob
        



