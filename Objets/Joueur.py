import Execution.affichageTextuel as affichageTextuel


class Joueur:
    def __init__(self, number, main):
        self.number = number
        self.main = main

    # Méthode qui dessine la main du joueur dans le terminal
    def afficher(self):
        print(f"Joueur {self.number} avec la main :")
        affichageTextuel.afficherMain(self.main)

    # Forme courte utilisée par print(joueur) et par l'affichage d'une liste
    def __repr__(self):
        return f"Joueur {self.number} avec la main: {self.main}"

    def get_number(self):
        return self.number

    def get_main(self):
        return self.main

    def str_main(self):
        if not self.main:
            return f"Main du joueur {self.number}:\n(main vide)"

        dominos = [str(domino) for domino in self.main]
        indices = [str(index) for index in range(len(dominos))]
        largeurs = [
            max(len(domino), len(index))
            for domino, index in zip(dominos, indices)
        ]
        ligne_dominos = " ".join(
            domino.center(largeur)
            for domino, largeur in zip(dominos, largeurs)
        )
        ligne_indices = " ".join(
            index.center(largeur)
            for index, largeur in zip(indices, largeurs)
        )
        return f"Main du joueur {self.number}:\n{ligne_dominos}\n{ligne_indices}"

    def add_main(self, piece):
        self.main.append(piece)

    def remove_main(self, piece):
        self.main.remove(piece)