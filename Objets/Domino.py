class Domino:
    # Constructeur de la classe Domino
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    # Méthode qui indique si le domino est un double
    def estDouble(self):
        return self.value1 == self.value2

    # Méthode qui retourne le dessin du domino sous forme de liste de lignes
    # vertical : True pour un domino debout, False pour un domino couché
    # inverse : True pour afficher value2 en premier (à gauche ou en haut)
    def dessin(self, vertical=False, inverse=False):
        premier, second = self.value1, self.value2
        if inverse:
            premier, second = second, premier

        if vertical:
            return [
                "┌───┐",
                f"│ {premier} │",
                "├───┤",
                f"│ {second} │",
                "└───┘"
            ]
        return [
            "┌───┬───┐",
            f"│ {premier} │ {second} │",
            "└───┴───┘"
        ]

    # Méthode qui dessine le domino dans le terminal, un print par ligne
    # Un double est affiché debout, les autres dominos sont couchés
    def afficher(self):
        for ligne in self.dessin(vertical=self.estDouble()):
            print(ligne)

    # Forme courte utilisée par print(domino) et par l'affichage d'une liste
    def __repr__(self):
        return f"[{self.value1}|{self.value2}]"

    # Méthode pour comparer deux dominos en utilisant l'opérateur ">"
    def __gt__(self, other):
        return self.value1 + self.value2 > other.value1 + other.value2

    # Méthode pour comparer deux dominos en utilisant l'opérateur "<"
    def __lt__(self, other):
        return self.value1 + self.value2 < other.value1 + other.value2

    def inverser(self):
            self.value1, self.value2 = self.value2, self.value1
