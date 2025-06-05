class Allenamento:

    def __init__(self, tipo, esercizi):
        self.tipo = tipo
        self.esercizi = esercizi

        return f"{self.tipo} con esercizi: {', '.join(self.esercizi)}"

class Professore: 

    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia

        return f"Professore {self.nome} di {self.materia}"


class Palestra(Allenamento, Professore):
    def __init__(self, tipo, esercizi, nome, materia):
        Allenamento.__init__(self, tipo, esercizi)
        Professore.__init__(self, nome, materia)

    def info(self):
       with open("C:\\Users\\lopon\\OneDrive\\Desktop\\account\\palestra.txt", "w") as file:
            file.write(f"Allenamento: {self.tipo}, Esercizi: {', '.join(self.esercizi)}, Professore: {self.nome}, Materia: {self.materia}\n")
        
partita = Palestra("Cardio", ["Corsa", "Bicicletta"], "Antonio", "Educazione Fisica")
partita.info()     
