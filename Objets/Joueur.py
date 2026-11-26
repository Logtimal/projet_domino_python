class Joueur:
    def __init__(self, number, main):
        self.number = number
        self.main = main

    def __str__(self):
        return f"Joueur {self.number} avec la main: {[str(domino) for domino in self.main]}"

    def get_number(self):
        return self.number

    def get_main(self):
        return self.main

    def add_main(self, piece):
        self.main.append(piece)

    def remove_main(self, piece):
        self.main.remove(piece)