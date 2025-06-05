## PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)

# Classe -> class seguita da nome in CamelCase per convenzione
# Attributi: dati e proprietà della classe
# Metodi: funzioni dentro la classe che determinano...

class NomeClasse:
    Attributo = "Attributo classe" # attributo di classe a cui tutti gli elementi hanno accesso

    def __init__(self, attributo1, attributo2):
        self.attributo1 = attributo1 # attributi di istanza
        self.attributo2 = attributo2

    def metodo(self):
        #azione dell'oggetto
        pass

# Instanziare oggetti classe:
# Definizione classe
# Chiamata al costruttore
# Creazione oggetto
# Utilizzo oggetto (accedere ad attributi e metodi)

class Cane:
    # costruzione
    def __init__(self, nome, eta):
        self.nome = nome #attributo nome
        self.eta = eta #attributo eta
    
    # medodo: azione che può fare
    def metodo(self):
        print(f"{self.nome} dice: Bau Bau!") # ?? si scrive così?

# variabili private: self.__attributo
# -> vedi ContoBancario

# Superclasse: contiene altre classi. Fa ereditare le proprietà alle classe figlie
# es: superclasse animale -> classe cane, classe gatto

class Cibo:
    def __init__(self, nome, calorie):
        self.nome = nome
        self.calorie = calorie

class Mela(Cibo):
    def mostra_info(self):
        print(f"Alimento {self.nome} ha {self.calorie} calorie.")

# Ridefinizione: una sottoclasse può ridefinire un metodo ereditato
# Estensione: aggiunge al metodo genitore

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def mostra_info(self):
        print(f"Auto {self.marca}, {self.modello}")

class Moto(Veicolo):
    def mostra_info(self):
        print(f"Moto {self.marca} {self.modello}")

Moto1 = Moto("BMW", "R 1300 GS")

# metodo STR: def __str__(self): definisce come la classe deve comportarsi quando chiamato come stringa

