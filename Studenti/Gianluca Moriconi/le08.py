#-----------------------------------------Esempio di composizione (has-a) in Python-------------------------------------
                # In questo esempio, la classe Auto ha una CinturaSicurezza, un Climatizzatore e un Motore.
"""
class CinturaSicurezza:   
    def allaccia(self):    
        print("Cintura ok.")

class Climatizzatore:   
    def accendi(self):    
        print("Climatizzatore ok.")
        
class Motore:   
    def start(self):    
        print("Motore avviato.")


class Auto:                                     # Composizione: Auto ha una Cintura, un Climatizzatore e un Motore
    def __init__(self):
        
        self.cintura = CinturaSicurezza()       # Auto ha una Cintura - richiamo del costruttore della classe Cintura
        self.climatizzatore = Climatizzatore()  # Auto ha un Climatizzatore - richiamo del costruttore della classe Climatizzatore
        self.motore = Motore()                  # Auto ha un Motore - richiamo del costruttore della classe Motore

                                # Metodi per interagire con gli oggetti Cintura, Climatizzatore e Motore

    def cintura_sic(self):                      # Metodo per allacciare la cintura di sicurezza         
        self.cintura.allaccia()
        

    def accendi_clima(self):                    # Metodo per accendere il climatizzatore
        self.climatizzatore.accendi()
        

    def guida(self):                            # Metodo per avviare il motore
        self.motore.start()
        

auto = Auto()
auto.cintura_sic()
auto.accendi_clima()
auto.guida()

"""
#----------------------------------------- ereditarietà e override + has-in ------------------------------------
                # In questo esempio, la classe Veicolo è la superclasse e le classi Auto e Bicicletta sono le sottoclassi.
"""
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def muovi(self):
        print("Il veicolo si sta muovendo.")



class Motore:
    def accendi(self):
        print("Motore avviato.")

class Stereo:
    def __init__(self, volume, brano, volume_max):
        self.volume = volume
        self.brano = brano
        self.volume_max = volume_max
   
    def suona(self):
        print("lo stereo si accende")
   
    def alza_volume(self):
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume alzato a {self.volume}.")
        else:
            print("Volume massimo raggiunto.")
   
    def abbassa_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume abbassato a {self.volume}.")
        else:
            print("Volume minimo raggiunto.")



class Auto(Veicolo):  
    def __init__(self, marca, modello):
        super().__init__(marca, modello)  # Chiamata al costruttore della superclasse Veicolo  
        self.marca = marca
        self.modello = modello
        self.motore = Motore()  # Composizione: Auto ha un Motore
        self.stereo = Stereo(5, "brano.mp3", 10)  # Composizione: Auto ha uno Stereo

    def accendi(self):
        print(f"L'auto {self.marca} {self.modello} si sta accendendo.")
        self.motore.accendi()
        self.stereo.suona()

    def muovi(self):
        print(f"L'auto {self.marca} {self.modello} si sta muovendo.")
        self.stereo.alza_volume()
        print(f"Volume attuale: {self.stereo.volume} ed il brano è: {self.stereo.brano}")


class Bicicletta(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca, modello) # Chiamata al costruttore della superclasse Veicolo
        self.marca = marca
        self.modello = modello
    def muovi(self):
        print(f"La bicicletta {self.marca} {self.modello} si sta muovendo.")



v= Veicolo("Generica", "Modello")  # Creazione di un oggetto della classe Veicolo
b = Bicicletta("Bianchi", "Corsa")  # Creazione di un oggetto della classe Bicicletta
a = Auto("Fiat", "500")          # Creazione di un oggetto della classe Auto






v.muovi()                 # Chiamata al metodo muovi della classe Veicolo
b.muovi()                # Chiamata al metodo muovi della classe Bicicletta
a.accendi() 
a.muovi()               # Chiamata al metodo muovi della classe Auto
"""

#----------------------------------------- Ereditarietà multipla -------------------------------------

class Veicolo:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

    def muovi(self):
        print("Il veicolo si sta muovendo.")


class Auto(Veicolo):  
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)  # Chiamata al costruttore della superclasse Veicolo  
        self.marca = marca
        self.tipo = tipo
    


class Bicicletta(Veicolo):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo) # Chiamata al costruttore della superclasse Veicolo
        self.marca = marca
        self.tipo = tipo

lista_veicoli = [ # Lista di veicoli con istanze di Auto e Bicicletta
    Auto("Fiat Panda", "Berlina"),    # Istanza di Auto
    Bicicletta("Bianchi", "Corsa"), # Istanza di Bicicletta
    Auto("Ferrari", "Sportiva"),
    Bicicletta("Canyon", "Mountain")
]

for veicolo in lista_veicoli:  # Iterazione sulla lista di veicoli
    veicolo.muovi()  # Chiamata al metodo muovi di ciascun veicolo
    if "Panda" in veicolo.marca:
        print(f"L'auto {veicolo.marca} ha la revisione in scadenza.")

#extra
lista_veicoli = []
numero_veicoli = int(input("Quanti veicoli vuoi inserire? "))

for i in range(numero_veicoli):
    tipo_oggetto = input("Inserisci il tipo di oggetto (Auto/Bicicletta): ").strip().lower()
    nome = input("Inserisci la marca del veicolo: ")
    tipo = input("Inserisci il tipo del veicolo: ")

    if tipo_oggetto == "auto":
        veicolo = Auto(nome, tipo)
    elif tipo_oggetto == "bicicletta":
        veicolo = Bicicletta(nome, tipo)
    else:
        print("Tipo di veicolo non valido. Inserimento saltato.")
        continue

lista_veicoli.append(veicolo)
for veicolo in lista_veicoli:
    veicolo.muovi()
    if isinstance(veicolo, Auto) and "Panda" in veicolo.marca:
        print(f"L'auto {veicolo.marca} ha la revisione in scadenza.")
    elif isinstance(veicolo, Bicicletta):
        print(f"La bicicletta {veicolo.marca} è pronta per essere pedalata.")