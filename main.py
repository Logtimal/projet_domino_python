import Execution.startGame as startGame
import Execution.game as game
nb_joueur = startGame.startGame()
joueurs, pioche = startGame.prepareGame(nb_joueur)

game.play_game(joueurs, pioche)

# Affichage de la main de chaque joueur
for joueur in joueurs:
    joueur.afficher()