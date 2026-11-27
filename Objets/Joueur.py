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

    def add_main(self, piece):
        self.main.append(piece)

    def remove_main(self, piece):
        self.main.remove(piece)