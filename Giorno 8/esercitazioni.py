class Veicolo:
    def __init__ (self, nome):
        self.nome = nome
    def muovi(self):
        print("il veicolo si sta muovendo")
        

class bicicletta(Veicolo):
    def muovi(self):
        print(f"La bicicletta di marca {self.nome} sta pedalando")

class auto(Veicolo):
    def __init__ (self, modello, nome):
        super().__init__(nome)
        self.modello = modello
    def muovi(self):
        print(f"L'auto di marca {self.nome} sta guidando")


v = Veicolo("aaa")
b = bicicletta("bbb")
a = auto("ccc", "ddd")

v.muovi()
b.muovi()
a.muovi()