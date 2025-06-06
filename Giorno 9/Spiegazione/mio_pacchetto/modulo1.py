class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def parla(self):
        return f"{self.nome} dice: Ciao!"
