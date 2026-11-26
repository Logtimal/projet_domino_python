import Execution.pioche as pioche
import random
# Fonction qui retourne le nombre de joueurs du jeu
def startGame():
    print("Combien de joueurs vont jouer ? (1 - 4)")
    nb_joueurs = int(input())
    if(nb_joueurs < 1 or nb_joueurs > 4):
        print("Le nombre de joueurs doit être compris entre 1 et 4.")
        return startGame()
    return nb_joueurs

# Fonction qui fait le préparation du jeu et retourne un tableau de joueurs et de la pioche
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
        



