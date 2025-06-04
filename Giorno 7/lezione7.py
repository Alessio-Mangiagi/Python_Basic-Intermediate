class Computer:
    def __init__(self, nome, marca, prezzo):
        self.nome = nome
        self.marca = marca
        self.prezzo = prezzo

    def info(self):
        return f"Nome: {self.nome}, Marca: {self.marca}, Prezzo: {self.prezzo}€"
    
class Ufficio:
    def __init__(self, nome, indirizzo):
        self.nome = nome
        self.indirizzo = indirizzo
    def info(self):
        return f"Nome: {self.nome}, Indirizzo: {self.indirizzo}"

class Laptop(Computer, Ufficio):
    def __init__(self, nome, marca, prezzo, nome_ufficio,indirizzo):
        Computer.__init__(self, nome, marca, prezzo)
        Ufficio.__init__(self, nome_ufficio, indirizzo )
    
    def info(self):
         with open("C:\\Users\\Alessio Mangiagi\\Desktop\\pythoncorso_riverloop\\Python_Basic-Intermediate\\Studenti\\Antonio Loponte\\file_prova1.txt", "w", encoding="utf-8") as f:
            f.write(f"{super().info()}, Ufficio: {self.nome}, Indirizzo: {self.indirizzo}\n")

Laptop1 = Laptop("ASUS", "ROG", 2200, "Ufficio1", "Via Roma 1")
Laptop2 = Laptop("Dell", "XPS", 1800, "Ufficio2", "Via Milano 2")