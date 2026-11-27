
import Execution.pioche as pioche
import random
import Objets.Joueur as Joueur


# Fonction qui retourne le nombre de joueurs du jeu
def startGame():
    print("Combien de joueurs vont jouer ? (1 - 4)")
    nb_joueurs = int(input())
    if(nb_joueurs < 1 or nb_joueurs > 4):
        print("Le nombre de joueurs doit être compris entre 1 et 4.")
        return startGame()
    return nb_joueurs

def prepareMainJoueur(nb_joueurs):
    piocheGlob = pioche.buildPioche()
    joueurs = []
    for i in range(nb_joueurs):
        joueurs.append(Joueur.Joueur(i + 1, i, [], [], []))
        for j in range(7):
            piece = pioche.drawDomino(piocheGlob)
            joueurs[i].add_main(piece)
            if piece.__gt__(joueurs[i].pieceForte):
                joueurs[i].set_pieceForte(piece)
            if piece.__lt__(joueurs[i].pieceFaible):
                joueurs[i].set_pieceFaible(piece)

    return joueurs, piocheGlob
    

# Fonction qui fait le préparation du jeu et retourne un tableau de joueurs et de la pioche
def prepareGame(nb_joueurs):
    joueurs, piocheGlob = prepareMainJoueur(nb_joueurs)
    if (joueurs[0].pieceForte.__lt__(joueurs[1].pieceForte)) :
        joueurs[1].set_ordre(1)
        joueurs[0].set_ordre(2)

    elif (joueurs[0].pieceForte.__gt__(joueurs[1].pieceForte)) :
        joueurs[0].set_ordre(1)
        joueurs[1].set_ordre(2)

    else :
        if (joueurs[0].pieceFaible.__lt__(joueurs[1].pieceFaible)) :
            joueurs[0].set_ordre(1)
            joueurs[1].set_ordre(2)

        elif (joueurs[0].pieceFaible.__gt__(joueurs[1].pieceFaible)) :
            joueurs[1].set_ordre(1)
            joueurs[0].set_ordre(2)
        
    return joueurs, piocheGlob
        



