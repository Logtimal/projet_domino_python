import Execution.affichageTextuel as affichageTextuel
def picher(pioche, joueur):
    if len(pioche) > 0:
        domino_pioché = pioche.pop()
        joueur.add_main(domino_pioché)
        print(f"Vous avez pioché le domino: {domino_pioché.value1} | {domino_pioché.value2}")
    else:
        print("La pioche est vide. Vous ne pouvez pas piocher.")

def add_domino_to_game(jeu, domino_choisi, joueur, first):
    if first:
        jeu.insert(0, domino_choisi)
    else:
        jeu.append(domino_choisi)
    joueur.remove_main(domino_choisi)

def arround_player(player, pioche, jeu):
    print("Voici le jeu actuel: ")
    # affichageTextuel.afficherPlateau(jeu)
    print("  ".join(f"{domino.value1} | {domino.value2}" for domino in jeu))
    print(player.str_main())
    print("Choisissez un domino à jouer (entrez l'index affiché dessous) ou -1 pour piocher :")
    while True:
        try:
            index = int(input())
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        if index == -1:
            picher(pioche, player)
            return
        if 0 <= index < len(player.get_main()):
            break
        print(
            f"Index invalide. Entrez un index entre 0 et "
            f"{len(player.get_main()) - 1}, ou -1 pour piocher."
        )

    domino_choisi = player.get_main()[index]
    if(len(jeu) == 0):
        add_domino_to_game(jeu, domino_choisi, player, first=True)
    else:
        if domino_choisi.value2 == jeu[0].value1:
            add_domino_to_game(jeu, domino_choisi, player, first=True)
        elif domino_choisi.value1 == jeu[0].value1:
            domino_choisi.inverser()
            add_domino_to_game(jeu, domino_choisi, player, first=True)
        elif domino_choisi.value1 == jeu[-1].value2:
            add_domino_to_game(jeu, domino_choisi, player, first=False)
        elif domino_choisi.value2 == jeu[-1].value2:
            domino_choisi.inverser()
            add_domino_to_game(jeu, domino_choisi, player, first=False)
        else:
            print("Le domino choisi ne peut pas être joué. Veuillez réessayer.")
            arround_player(player, pioche, jeu)

def play_game(players, pioche):
    win = False
    jeu = []

    while not win:
        for joueur in players:
            print("C'est au tour du joueur " + str(joueur.get_number()) + " de jouer.")
            # Logique de jeu pour le joueur actuel
            arround_player(joueur, pioche, jeu)
            if len(joueur.get_main()) == 0:
                print("Le joueur " + str(joueur.get_number()) + " a gagné !")
                win = True
                break
