# Crea una lista di veicoli che contiene sia oggetti Bicicletta che oggetti auto.
# Usa un ciclo for per muovere tutti i veicoli nella lista.
# Se il nome del veicolo contiene la parola "Panda", stampiamo "revisione in scadenza."
# extra chiediamo al utente quanti veicoli vuole inserire e i loro dati (nome e tipo), poi esegui le azioni su tutti i veicoli.


class Veicolo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def muovi(self):
        print("Il veicolo si sta muovendo")


class Clacson:
    def suona(self):
        print("Il clacson suona: Beep beep!")


class Auto(Veicolo):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        self.clacson = Clacson()

    def muovi(self):
        print(f"L'auto di marca {self.nome} sta guidando ed è di tipo {self.tipo}")
        self.clacson.suona()


class Trombetta:
    def suona(self):
        print("La trombetta suona: Beep beep!")


class Bicicletta(Veicolo):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        self.trombetta = Trombetta()

    def muovi(self):
        print(
            f"La bicicletta di marca {self.nome} sta pedalando ed è di tipo {self.tipo}"
        )
        self.trombetta.suona()


# normale
# lista_veicoli = [Auto("Fiat Panda", "Benzina"),Bicicletta("Bianchi", "Mountain Bike"),Auto("Fiat 500", "Elettrica"),Bicicletta("Cicli Rossi", "Strada"),]


# extra
lista_veicoli = []
numero_veicoli = int(input("Quanti veicoli vuoi inserire? "))

for n in range(numero_veicoli):
    tipo_oggetto = input("Inserisci il tipo di oggetto (Auto/Bicicletta):")
    nome = input("Inserisci il nome del veicolo: ")
    tipo = input("Inserisci il tipo del veicolo: ")

    if tipo_oggetto.lower() == "auto":
        veicolo = Auto(nome, tipo)
    elif tipo_oggetto.lower() == "bicicletta":
        veicolo = Bicicletta(nome, tipo)
    else:
        print("Tipo di veicolo non riconosciuto. Inserimento saltato.")
        continue

    lista_veicoli.append(veicolo)

for veicolo in lista_veicoli:
    veicolo.muovi()
    if "Panda" in veicolo.nome:
        print("Revisione in scadenza per", veicolo.nome)
