class animale:
    def __init__(self, nome, eta, colore):
        self.nome = nome
        self.eta = eta
        self.colore = colore

class gatto(animale):
   def miagola(self):
        print(f"Il gatto {self.nome} di colore {self.colore} miagola.")
ilmiogatto = gatto("Pallina", 7, "grigio e bianco")
ilmiogatto.miagola()

class tartaruga(animale):
    def morde(self):
        print(f"La tartaruga {self.nome} di colore {self.colore} morde le dita dei piedi.")

lamiatartaruga = tartaruga("Tartosso", 21, "verde")
lamiatartaruga.morde()


        

    

    