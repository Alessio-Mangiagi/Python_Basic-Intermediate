class Cane:
    # Costruttore: serve per inizializzare l'oggetto
    zampe = 4  # attributo di classe, comune a tutti i cani
    
    def __init__(self, nome, eta):
        self.nome = nome  # attributo nome  
        self.eta = eta  # attributo eta
        
    def  __str__(self):
        return f"il Cane si chiama {self.nome}, ha {self.eta} anni ed ha {self.zampe} zampe"
    
    # Metodo: azione che il cane può fare
    def abbaia(self):
        print(f"{self.nome} dice: Bau Bau!")

    def seduto(self):
        print(f"{self.nome} si siede.")


mio_cane = Cane("Fido", 3)
cane_di_giada = Cane("Ulisse", 6)

print(cane_di_giada)
