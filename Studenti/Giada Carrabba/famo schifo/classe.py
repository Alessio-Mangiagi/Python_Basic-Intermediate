class animale:
    def __init__(self, nome, eta, colore):
        self.nome = nome
        self.eta = eta
        self.colore = colore
        


class gatto(animale): 
    
        
    def miagola(self):
        print("il gatto " + self.nome + " miagola ed ha " + self.eta + " anni e il suo colore è " + self.colore)

ilmiogatto = gatto (" pippo ", " 10 " , " nero ")
ilmiogatto.miagola()  

class cane(animale):
    def __init__(self, nome, eta, colore, razza):
        super().__init__(nome, eta, colore)
        self.razza = razza
    def abbaia(self):
        print("il cane " + self.nome + " abbaia ed ha " + str(self.eta) + " anni e la sua razza è " + self.razza)

ilmiocane = cane(" ulysse ", 5 , " marrone ", " labrador ")
ilmiocane.abbaia()

