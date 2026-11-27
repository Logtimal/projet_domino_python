import Execution.affichageTextuel as affichageTextuel


class Joueur:
    def __init__(self, number, main):
        self.number = number
        self.main = main

    def __str__(self):
        lignes = affichageTextuel.construireMain(self.main)
        return "\n".join([f"Joueur {self.number} avec la main :"] + lignes)

    def get_number(self):
        return self.number

    def get_main(self):
        return self.main

    def add_main(self, piece):
        self.main.append(piece)

    def remove_main(self, piece):
        self.main.remove(piece)