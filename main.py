import Execution.startGame as startGame
nb_joueur = startGame.startGame()
joueurs, pioche = startGame.prepareGame(nb_joueur)

# Affichage de la main de chaque joueur
for joueur in joueurs:
    print(joueur)