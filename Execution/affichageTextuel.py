# Largeur maximale du plateau, en nombre de caractères
LARGEUR_MAX = 60
# Largeur minimale acceptée : la place de deux dominos couchés
LARGEUR_MIN = 18


# Fonction qui place chaque domino du plateau
# Retourne une liste de tuples (x, y, dessin), (x, y) étant le coin haut gauche
# Le plateau serpente de bas en haut : la première ligne va vers la droite,
# puis chaque nouvelle ligne repart dans l'autre sens
def placerDominos(plateau, largeur_max):
    placements = []
    sens = 1            # 1 : vers la droite, -1 : vers la gauche
    bord = 0            # colonne où se colle le prochain domino
    axe = 0             # hauteur du milieu de la ligne en cours
    haut_coin = None    # haut du domino de virage qui vient d'être posé
    demi_hauteur = 0    # demi-hauteur du dernier domino posé sur la ligne

    for domino in plateau:
        # Les doubles sont debout, les autres couchés (retournés vers la gauche)
        dessin = domino.dessin(vertical=domino.estDouble(), inverse=(sens == -1))
        largeur = len(dessin[0])
        hauteur = len(dessin)

        # La nouvelle ligne se pose juste au-dessus du domino de virage
        if haut_coin is not None:
            axe = haut_coin - 1 - hauteur // 2
            haut_coin = None

        if sens == 1:
            depasse = bord + largeur > largeur_max
        else:
            depasse = bord - largeur < 0

        if depasse:
            # Virage : le domino est posé debout au-dessus du bout de la ligne,
            # avec value1 en bas (côté domino précédent) et value2 en haut
            dessin = domino.dessin(vertical=True, inverse=True)
            largeur = len(dessin[0])
            x = bord - largeur if sens == 1 else bord
            y = axe - demi_hauteur - len(dessin)
            placements.append((x, y, dessin))
            haut_coin = y
            # Demi-tour : la ligne suivante part du même côté que le virage
            bord = x + largeur if sens == 1 else x
            sens = -sens
        else:
            x = bord if sens == 1 else bord - largeur
            y = axe - hauteur // 2
            placements.append((x, y, dessin))
            bord = bord + sens * largeur
            demi_hauteur = hauteur // 2

    return placements


# Fonction qui retourne les lignes de texte représentant le plateau
def construirePlateau(plateau, largeur_max=LARGEUR_MAX):
    if largeur_max < LARGEUR_MIN:
        raise ValueError(f"La largeur maximale doit être d'au moins {LARGEUR_MIN}.")
    if len(plateau) == 0:
        return []

    placements = placerDominos(plateau, largeur_max)
    haut = min(y for x, y, dessin in placements)
    bas = max(y + len(dessin) for x, y, dessin in placements)

    # Grille de caractères vide sur laquelle on recopie chaque domino
    grille = [[" "] * largeur_max for i in range(bas - haut)]
    for x, y, dessin in placements:
        for i, ligne in enumerate(dessin):
            for j, caractere in enumerate(ligne):
                grille[y - haut + i][x + j] = caractere

    return ["".join(ligne).rstrip() for ligne in grille]


# Fonction qui affiche le plateau
def afficherPlateau(plateau, largeur_max=LARGEUR_MAX):
    if len(plateau) == 0:
        print("Le plateau est vide.")
        return

    for ligne in construirePlateau(plateau, largeur_max):
        print(ligne)
