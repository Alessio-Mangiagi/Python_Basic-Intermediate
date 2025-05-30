class Alunno:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni"

    def __repr__(self):
        return f"Alunno({self.nome!r}, {self.cognome!r}, {self.eta!r})"
    

if __name__ == "__main__":
        alunno1 = Alunno("Antonio", "Loponte", 25)
        alunno2 = Alunno("Massimiliano", "Zanato", 30)
        
        print(alunno1)
        print(alunno2)
        
        alunni = [alunno1, alunno2]
        print(alunni)