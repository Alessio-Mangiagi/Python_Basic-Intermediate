# ===========================
# Definizione Classi Animali
# ===========================

from animal_pack.messages import Animal_act

class Animali:                  # classe generica per assegnare "nome" ad ogni animale
    def __init__(self, nome, lingua):
        self.nome = nome
        self.lingua = lingua
    
    def exit(self):             # comune a tutti gli animali. Interazione alla chiusura del gioco.
        msg = Animal_act["General"]["exit"][self.lingua].format(nome=self.nome)
        print(msg)

class Cane(Animali):
    def __init__(self, nome, lingua):
        super().__init__(nome, lingua)

    def parla(self):
        msg = Animal_act["Cane"]["parla"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def seduto(self):
        msg = Animal_act["Cane"]["seduto"][self.lingua].format(nome=self.nome)
        print(msg)

    def terra(self):
        msg = Animal_act["Cane"]["terra"][self.lingua].format(nome=self.nome)
        print(msg)

    def bravo(self):
        msg = Animal_act["Cane"]["bravo"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def biscotto(self):
        msg = Animal_act["Cane"]["biscotto"][self.lingua].format(nome=self.nome)
        print(msg)

    def osserva(self):
        msg = Animal_act["Cane"]["osserva"][self.lingua].format(nome=self.nome)
        print(msg)

class Gatto(Animali):
    def parla(self):
        msg = Animal_act["Gatto"]["parla"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def seduto(self):
        msg = Animal_act["Gatto"]["seduto"][self.lingua].format(nome=self.nome)
        print(msg)

    def terra(self):
        msg = Animal_act["Gatto"]["terra"][self.lingua].format(nome=self.nome)
        print(msg)

    def bravo(self):
        msg = Animal_act["Gatto"]["bravo"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def biscotto(self):
        msg = Animal_act["Gatto"]["biscotto"][self.lingua].format(nome=self.nome)
        print(msg)

    def osserva(self):
        msg = Animal_act["Gatto"]["osserva"][self.lingua].format(nome=self.nome)
        print(msg)

class Pesce(Animali):
    def parla(self):
        msg = Animal_act["Pesce"]["parla"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def seduto(self):
        msg = Animal_act["Pesce"]["seduto"][self.lingua].format(nome=self.nome)
        print(msg)

    def terra(self):
        msg = Animal_act["Pesce"]["terra"][self.lingua].format(nome=self.nome)
        print(msg)

    def bravo(self):
        msg = Animal_act["Pesce"]["bravo"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def biscotto(self):
        msg = Animal_act["Pesce"]["biscotto"][self.lingua].format(nome=self.nome)
        print(msg)

    def osserva(self):
        msg = Animal_act["Pesce"]["osserva"][self.lingua].format(nome=self.nome)
        print(msg)

class Pappagallo(Animali):
    def parla(self):
        msg = Animal_act["Pappagallo"]["parla"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def seduto(self):
        msg = Animal_act["Pappagallo"]["seduto"][self.lingua].format(nome=self.nome)
        print(msg)

    def terra(self):
        msg = Animal_act["Pappagallo"]["terra"][self.lingua].format(nome=self.nome)
        print(msg)

    def bravo(self):
        msg = Animal_act["Pappagallo"]["bravo"][self.lingua].format(nome=self.nome)
        print(msg)
    
    def biscotto(self):
        msg = Animal_act["Pappagallo"]["biscotto"][self.lingua].format(nome=self.nome)
        print(msg)

    def osserva(self):
        msg = Animal_act["Pappagallo"]["osserva"][self.lingua].format(nome=self.nome)
        print(msg)