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

    # Méthode pour représenter le domino sous forme de chaîne de caractères
    # Un double est affiché debout, les autres dominos sont couchés
    def __str__(self):
        return "\n".join(self.dessin(vertical=self.estDouble()))

    # Forme courte utilisée par Python quand on affiche une liste de dominos
    def __repr__(self):
        return f"[{self.value1}|{self.value2}]"

    # Méthode pour comparer deux dominos en utilisant l'opérateur ">"
    def __gt__(self, other):
        return self.value1 + self.value2 > other.value1 + other.value2

    # Méthode pour comparer deux dominos en utilisant l'opérateur "<"
    def __lt__(self, other):
        return self.value1 + self.value2 < other.value1 + other.value2
