# ereditarietà di base:
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print("Questo animale fa un verso.")


class Cane(Animale):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Bassotto"

    def parla(self):
        print(f"{self.nome} che è un {self.tipo} dice: Bau bau!")


class Gatto(Animale):
    def parla(self):
        print(f"{self.nome} dice: Miao!")


il_mio_cane = Cane("Fido")
il_mio_cane.parla()  # Fido dice: Bau bau!
il_mio_gatto = Gatto("Micia")
il_mio_gatto.parla()  # Micia dice: Miao!


class Abbigliamento:
    def __init__(self, colore, taglia):
        self.colore = colore
        self.taglia = taglia

    def mostra_info(self):
        print(f"Vestito di colore {self.colore} e taglia {self.taglia}.")


class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def mostra_info(self):
        print(f"Prodotto {self.nome} al prezzo di {self.prezzo} euro.")


class Camicia(Abbigliamento, Prodotto):
    def __init__(self, colore, taglia, nome, prezzo):
        Abbigliamento.__init__(self, colore, taglia)
        Prodotto.__init__(self, nome, prezzo)

    def mostra_info(self):
        print(
            f"Camicia di colore {self.colore}, taglia {self.taglia}, "
            f"nome {self.nome} e prezzo {self.prezzo} euro."
        )


class Pantaloni(Abbigliamento):
    def mostra_info(self):
        print(f"Pantaloni di colore {self.colore} e taglia {self.taglia}.")


class Maglietta(Abbigliamento):
    def mostra_info(self):
        print(f"Maglietta di colore {self.colore} e taglia {self.taglia}.")


abbigliamento1 = Camicia("Blu", "M", "Camicia Elegante", 29.99)
abbigliamento1.mostra_info()  # Camicia di colore Blu e taglia M.


class Cibo:
    def __init__(self, nome, calorie):
        self.nome = nome
        self.calorie = calorie

    def mostra_info(self):
        print(f"Cibo {self.nome} con {self.calorie} calorie.")


class Mela(Cibo):
    def mostra_info(self):
        print(f"Mela {self.nome} con {self.calorie} calorie.")


class Pizza(Cibo):
    def mostra_info(self):
        print(f"Pizza {self.nome} con {self.calorie} calorie.")


class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_info(self):
        print(f"Veicolo {self.marca} {self.modello}.")


class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def mostra_info(self):
        print(f"Prodotto {self.nome} al prezzo di {self.prezzo} euro.")


class Auto(Veicolo, Prodotto):
    def __init__(self, marca, modello, nome, prezzo):
        Veicolo.__init__(self, marca, modello)
        Prodotto.__init__(self, nome, prezzo)

    def mostra_info(self):
        print(
            f"Auto {self.marca} {self.modello}, "
            f"nome {self.nome} e prezzo {self.prezzo} euro."
        )


class Moto(Veicolo):
    def mostra_info(self):
        print(f"Moto {self.marca} {self.modello}.")


class Elettrodomestico:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_info(self):
        print(f"Elettrodomestico: {self.marca} {self.modello}.")


class ProdottoElettrodomestico:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def mostra_info(self):
        print(f"Prodotto Elettrodomestico {self.nome} al prezzo di {self.prezzo} euro.")


class Lavatrice(Elettrodomestico, ProdottoElettrodomestico):
    def __init__(self, marca, modello, carico):
        super().__init__(marca, modello)
        ProdottoElettrodomestico.__init__(self, "Lavatrice", 499.99)
        self.carico = carico

    def mostra_info(self):
        print(
            f"Lavatrice {self.marca} {self.modello}, carico {self.carico} kg, "
            f"nome {self.nome} e prezzo {self.prezzo} euro."
        )


class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, capacita):
        super().__init__(marca, modello)
        self.capacita = capacita

    def mostra_info(self):
        print(
            f"Frigorifero {self.marca} {self.modello}, capacità {self.capacita} litri."
        )


Lavatrice1 = Lavatrice("Bosch", "Serie 4", 8)
Lavatrice1.mostra_info()  # Lavatrice Bosch Serie 4, carico 8 kg.
