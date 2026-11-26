class Domino:
    # Constructeur de la classe Domino
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    # Méthode pour représenter le domino sous forme de chaîne de caractères
    def __str__(self):
        return f"[{self.value1}|{self.value2}]"

    # Méthode pour comparer deux dominos en utilisant l'opérateur ">"
    def __gt__(self, other):
        return self.value1 + self.value2 > other.value1 + other.value2

    # Méthode pour comparer deux dominos en utilisant l'opérateur "<"
    def __lt__(self, other):
        return self.value1 + self.value2 < other.value1 + other.value2