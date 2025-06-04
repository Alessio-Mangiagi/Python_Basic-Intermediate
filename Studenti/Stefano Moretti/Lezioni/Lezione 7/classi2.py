class Vestito:
    def __init__(self, colore, taglia): 
        self.colore = colore
        self.taglia = taglia

    def mostra_info(self):
        print(f"Vestito di colore {self.colore} e taglia {self.taglia}")

class Camicia(Vestito):
    def mostra_info(self):
        print(f"Camicia di colore {self.colore} e taglia {self.taglia}")

class Pantaloni(Vestito):
    def mostra_info(self):
        print(f"Pantaloni di colore {self.colore} e taglia {self.taglia}")

class Giacca(Vestito):
    def mostra_info(self):
        print(f"Giacca di colore {self.colore} e taglia {self.taglia}")

vestito1 = Camicia("Blu", "M")
vestito2 = Pantaloni("Nero", "M")
vestito1.mostra_info()
vestito2.mostra_info()

