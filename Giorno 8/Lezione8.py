class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print("L'animale fa un verso.")


class Cane(Animale):
    def __init__(self, nome, razza):
        # Richiama il costruttore della classe genitore
        super().__init__(nome)
        self.razza = razza

    def parla(self):
        # Puoi richiamare il metodo parla della classe genitore (opzionale)
        super().parla()
        print(f"{self.nome} ({self.razza}) dice: Bau bau!")


# Utilizzo
# c = Cane("Fido", "Bassotto")
# c.parla()


class Veicolo:
    def __init__(self, modello, n_posti):
        self.modello = modello
        self.n_posti = n_posti

    def accendi(self):
        print("veicolo acceso. modello:", self.modello, "posti:", self.n_posti)


class Auto(Veicolo):
    def accendi(self):
        super().accendi()  # Richiama il metodo accendi della classe genitore
        print("Auto accesa. Pronta a partire!")


# a = Auto("Fiat 500", 4)
# a.accendi()


class Motore:
    def avvia(self):
        print("Motore avviato.")


class Radio:
    def __init__(self):
        self.stazione = "Radio 1"

    def set_stazione(self, stazione):
        self.stazione = stazione
        print(f"Stazione radio impostata su {self.stazione}.")

    def accendi(self):
        print("Radio accesa. Buon ascolto!")


class CinturaSicurezza:
    def allaccia(self):
        print("Cintura di sicurezza allacciata. Sicurezza prima di tutto!")


class Climatizzatore:
    def __init__(self):
        self.temperatura = 22
        self.modalita = "automatico"

    def set_temperatura(self, temperatura):
        self.temperatura = temperatura
        print(f"Temperatura impostata a {self.temperatura} gradi.")

    def accendi(self):
        print("Climatizzatore acceso. Temperatura ottimale!")


class Automobile:
    def __init__(self):
        self.motore = Motore()
        self.radio = Radio()
        self.cintura = CinturaSicurezza()
        self.climatizzatore = Climatizzatore()

    def accendi(self):
        self.motore.avvia()
        self.radio.accendi()
        self.cintura.allaccia()
        self.climatizzatore.accendi()
        self.climatizzatore.set_temperatura(18)
        print("Automobile pronta!")


auto = Automobile()
auto.accendi()

# Output:
# Motore avviato.
# Automobile pronta!
