class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def parla(self):
        return f"{self.nome} dice: Ciao!"


from .modulo2 import Saluta


def ParlaGenerico():
    print("Questo è un metodo generico di un pacchetto.")
    Saluta()
