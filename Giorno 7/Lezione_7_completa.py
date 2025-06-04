class Cane:
    # Costruttore: serve per inizializzare l'oggetto
    def __init__(self, nome, eta):
        self.nome = nome  # attributo nome
        self.eta = eta  # attributo eta

    # Metodo: azione che il cane può fare
    def abbaia(self):
        print(f"{self.nome} dice: Bau Bau!")

    def Seduto(self):
        print(f"{self.nome} si siede.")


mio_cane = Cane("Fido", 3)
mio_cane.abbaia()  # Output: Fido dice: Bau Bau!


# schema di una classe riassuntivo:


class NomeClasse:
    def __init__(self, attributo1, attributo2):
        self.attributo1 = attributo1
        self.attributo2 = attributo2

    def metodo(self):
        # Azione dell’oggetto
        print("")


class Ricetta:
    Chef = "Chef Mario"  # attributo di classe

    def __init__(self, nome, ingredienti):
        self.nome = nome  # attributo di istanza
        self.ingredienti = ingredienti  # attributo di istanza

    def mostra_ricetta(self):
        print(f"Ricetta: {self.nome} di {self.Chef}")
        print("Ingredienti:")
        for ingrediente in self.ingredienti:
            print(f"- {ingrediente}")


ricetta1 = Ricetta(
    "Pasta al Pomodoro", ["Pasta", "Pomodoro", "Olio d'oliva", "Basilico"]
)
ricetta2 = Ricetta("Insalata di Riso", ["Riso", "Pomodorini", "Mozzarella", "Olive"])

ricetta1.mostra_ricetta()


# attributi di una classe vs attributi di instance:
class Studente2:
    scuola = "Liceo Classico"  # attributo di classe

    def __init__(self, nome, eta):
        self.nome = nome  # attributo di istanza
        self.eta = eta


# Ogni studente ha il suo nome e la sua età, ma condividono la stessa scuola
s1 = Studente2("Giulia", 17)
s2 = Studente2("Marco", 18)
print(s1.nome, s1.scuola)  # Giulia Liceo Classico
print(s2.nome, s2.scuola)  # Marco Liceo Classico


# incapsulamento attributi privati


class ContoBancario:
    def __init__(self, titolare, saldo):
        self.titolare = titolare
        self.__saldo = saldo  # attributo privato

    def deposita(self, importo):
        self.__saldo += importo

    def preleva(self, importo):
        if importo <= self.__saldo:
            self.__saldo -= importo
        else:
            raise ValueError("Saldo insufficiente per il prelievo")

    def mostra_saldo(self):
        return self.__saldo


conto1 = ContoBancario("Alice", 1000)

print(conto1.mostra_saldo())


# Uso:
conto = ContoBancario("Alice", 1000)
conto.deposita(500)
print(conto.mostra_saldo())  # 1500
# print(conto.__saldo)  # Errore! Attributo privato


# esempio di classe con metodo __str__ per la rappresentazione in stringa:
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"'{self.titolo}' di {self.autore}"


libro = Libro("Il Piccolo Principe", "Saint-Exupéry")

print(libro)  # 'Il Piccolo Principe' di Saint-Exupéry


# ereditarietà di base:
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print("Questo animale fa un verso.")


class Cane(Animale):
    def parla(self):
        print(f"{self.nome} dice: Bau bau!")


class Gatto(Animale):
    def parla(self):
        print(f"{self.nome} dice: Miao!")


# Uso:
fido = Cane("Fido")
fido.parla()  # Fido dice: Bau bau!
micia = Gatto("Micia")
micia.parla()  # Micia dice: Miao!


# uso di super()
class Persona:
    def __init__(self, nome):
        self.nome = nome


class Studente(Persona):
    def __init__(self, nome, classe):
        super().__init__(nome)
        self.classe = classe


s = Studente("Paolo", "3B")
print(s.nome, s.classe)  # Paolo 3B


# override di metodi:
class Veicolo:
    def accendi(self):
        print("Veicolo acceso.")


class Auto(Veicolo):
    def accendi(self):
        print("Auto accesa. Pronta a partire!")


v = Veicolo()
v.accendi()  # Veicolo acceso.

a = Auto()
a.accendi()  # Auto accesa. Pronta a partire!


# composizione di classi:


class Motore:
    def avvia(self):
        print("Motore avviato.")


class Automobile:
    def __init__(self):
        self.motore = Motore()

    def accendi(self):
        self.motore.avvia()
        print("Automobile pronta!")


auto = Automobile()
auto.accendi()
# Output:
# Motore avviato.
# Automobile pronta!
