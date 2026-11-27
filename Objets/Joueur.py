import Execution.affichageTextuel as affichageTextuel


class Joueur:
    def __init__(self, number, ordre, pieceForte, pieceFaible, main):
        self.number = number
        self.ordre = ordre
        self.pieceForte = pieceForte
        self.pieceFaible = pieceFaible
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

    def set_ordre(self, num):
        self.ordre = num

    def get_ordre(self):
        return self.ordre

    def get_main(self):
        return self.main

    def get_pieceForte(self):
        return self.pieceForte

    def set_pieceForte(self, piece):
        self.pieceForte = piece

    def get_pieceFaible(self):
        return self.pieceFaible

    def set_pieceFaible(self, piece):
        self.pieceFaible = piece

    def add_main(self, piece):
        self.main.append(piece)

    def remove_main(self, piece):
        self.main.remove(piece)