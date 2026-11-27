import Execution.affichageTextuel as affichageTextuel
def picher(pioche, joueur):
    if len(pioche) > 0:
        domino_pioché = pioche.pop()
        joueur.add_main(domino_pioché)
        print(f"Vous avez pioché le domino: {domino_pioché.value1} | {domino_pioché.value2}")
    else:
        print("La pioche est vide. Vous ne pouvez pas piocher.")

def add_domino_to_game(jeu, domino_choisi, joueur, first, need_invert=False):
    if need_invert:
        domino_choisi.inverser()
    if first:
        jeu.insert(0, domino_choisi)
    else:
        jeu.append(domino_choisi)
    joueur.remove_main(domino_choisi)

def verify_right(domino_choisi, jeu):
    if(domino_choisi.value2 == jeu[0].value1):
        return True, False
    elif(domino_choisi.value1 == jeu[0].value1):
        return True, True
    return False, False

def verify_left(domino_choisi, jeu):
    if(domino_choisi.value1 == jeu[-1].value2):
        return True, False
    elif(domino_choisi.value2 == jeu[-1].value2):
        return True, True
    return False, False

def arround_player(player, pioche, jeu):
    print("Voici le jeu actuel: ")
    # affichageTextuel.afficherPlateau(jeu)
    print("  ".join(str(domino) for domino in jeu))    
    print(player.afficher())
    print("Choisissez un domino à jouer (entrez l'index affiché dessous) ou -1 pour piocher :")
    while True:
        try:
            index = int(input())
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        if index == -1:
            picher(pioche, player)
            arround_player(player, pioche, jeu)
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
        if verify_right(domino_choisi, jeu)[0] and verify_left(domino_choisi, jeu)[0]:
            print("Le domino choisi peut être joué à gauche ou à droite. Où voulez-vous le jouer ? (gauche/droite)")
            while True:
                choix = input().lower()
                if choix == "gauche":
                    add_domino_to_game(jeu, domino_choisi, player, first=True)
                    break
                elif choix == "droite":
                    add_domino_to_game(jeu, domino_choisi, player, first=False)
                    break
                else:
                    print("Veuillez entrer 'gauche' ou 'droite'.")
        elif verify_right(domino_choisi, jeu)[0]:
            add_domino_to_game(jeu, domino_choisi, player, first=True, need_invert=verify_right(domino_choisi, jeu)[1])
        elif verify_left(domino_choisi, jeu)[0]:
            add_domino_to_game(jeu, domino_choisi, player, first=False, need_invert=verify_left(domino_choisi, jeu)[1])
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
