import pandas as pd

# Lista di veicolo che contiene bicicletta e oggetti auto
# usa ciclo for per muovere tutti i veicoli nella lista.
# Se il nome del veicolo contiene "panda" stampiamo: "revisione in scadenza"
# extra: chiediamo all'utente quanti veicoli vuole inserire
# poi esegui azioni su tutti i veicoli.

class Veicolo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def muovi(self):
        print("Il veicolo si sta muovendo")

class Auto(Veicolo):
    def muovi(self):
        print(f"L'auto di marca {self.nome} sta guidando ed è di tipo {self.tipo}")

class Bicicletta(Veicolo):
    def muovi(self):
        print(f"La bicicletta di marca {self.nome} sta pedalando ed è di tipo {self.tipo}")


n_veicoli = int(input("Quanti veicoli vuoi inserire? (numero)"))
lista_veicoli = []

for veicolo in range(n_veicoli):
    tipo_oggetto = input("Il veicolo è un'auto o bicicletta? ")
    nome = input("Inserisci il nome del veicolo: ")
    tipo = input("Inserisci il tipo del veicolo: ")

    if tipo_oggetto.lower() == "auto":
        veicolo = Auto(nome, tipo)
    elif tipo_oggetto.lower() == "bicicletta":
        veicolo = Bicicletta(nome, tipo)
    else:
        print("Tipo di veicolo non riconosciuto. Scegli tra Auto o Bicicletta")
    
    lista_veicoli.append(veicolo)

for veicolo in lista_veicoli:
    veicolo.muovi()
    if "Panda" in veicolo.nome:
        print("Revisione in scadenza per", veicolo.nome)