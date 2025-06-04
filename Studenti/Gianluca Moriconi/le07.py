class Computer:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def info(self):
        return f"Computer: {self.name}, Price: {self.price}, Brand: {self.brand}"
    
class Ufficio:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def info(self):
        return f"Ufficio: {self.name}, Address: {self.address}"
    
class ComputerUfficio(Computer, Ufficio):       # ComputerUfficio eredita da Computer e Ufficio
    def __init__(self, name, price, brand, address):
        super().__init__(name, price, brand)    # Richiamo il costruttore della classe Computer. Senza funzione super(), avrei dovuto scrivere self su init come Ufficio
        Ufficio.__init__(self, name, address)   # Richiamo il costruttore della classe Ufficio

    def info(self):                             # Override del metodo info per ComputerUfficio
        with open("/home/gianluca/repos/Riverloop - Python/Python_Basic-Intermediate/Studenti/Gianluca Moriconi/log.txt", "w", encoding="utf-8") as file: 
                                                # Apri il file in modalità scrittura per registrare le informazioni
            file.write(f"ComputerUfficio: {self.name}, Price: {self.price}, Brand: {self.brand}, Address: {self.address}\n") 
                                                # Scrivi le informazioni nel file
      
laptop1 = ComputerUfficio("Dell XPS 13", 1200, "Dell", "123 Main St") # Creazione di un'istanza di ComputerUfficio
laptop1.info()                                  # Chiamata al metodo info per registrare le informazioni nel file


class gatto:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def miagola(self):
       print(f"{self.nome} dice: Miao!")
il_mio_gatto = gatto("Whiskers", 3)  # Creazione di un'istanza della classe gatto
il_mio_gatto.miagola()                # Chiamata al metodo miagola per il gatto

class cane:
    def __init__(self, nome, razza):
        self.nome = nome
        self.razza = razza
    def abbaia(self):
       print(f"{self.nome} dice: Bau!")
    def abbaia(self):
       print(f"{self.nome} dice: Bau!")
il_mio_cane = cane("Fido", "pastore tedesco")        # Creazione di un'istanza della classe cane
il_mio_cane.abbaia()                  # Chiamata al metodo abbaia per il cane