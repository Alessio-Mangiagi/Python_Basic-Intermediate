class Veicolo:
    def __init__(self, nome):
        self.nome = nome

    def muovi(self):
        print("il veicolo si sta muovendo")


class bicicletta(Veicolo):
    def muovi(self):
        print(f"La bicicletta di marca {self.nome} sta pedalando")


class motore:
    def accendi(self):
        print("Il motore si sta accendendo")


class stereo:
    def __init__(self, volume, brano, volume_max):
        self.volume = volume
        self.brano = brano
        self.volume_max = volume_max

    def accendi(self):
        print("Lo stereo si sta accendendo")

    def alza_volume(self):
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume alzato a {self.volume}")
            if self.volume > 5:
                print("Attenzione: volume troppo alto, potrebbe danneggiare l'udito!")
        else:
            print("Volume massimo raggiunto")


class auto(Veicolo):
    def __init__(self, modello, nome, stereo):
        super().__init__(nome)
        self.modello = modello
        self.motore = motore()
        self.stereo = stereo

    def accendi(self):
        print(f"L'auto di marca {self.nome} si sta accendendo")
        self.motore.accendi()
        self.stereo.accendi()

    def muovi(self):
        print(f"L'auto di marca {self.nome} sta guidando")
        self.stereo.alza_volume()
        print(f"Il brano attualmente in riproduzione è: {self.stereo.brano}")


v = Veicolo("aaa")
b = bicicletta("bbb")
a = auto("ccc", "ddd", stereo(6, "Brano preferito", 10))


v.muovi()
b.muovi()
a.accendi()
a.muovi()
