class gatto: 
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta 
    def miagola(self):
        print(" il gatto " + self.nome + " miagola ")
ilmiogatto = gatto (" pippo ", " 10 ")
ilmiogatto.miagola()  

class cane:
    def __init__(self,nome, razza):
        self.nome = nome
        self.razza = razza 
    def abbaia(self):
        print ("il cane " + self.nome + " abbaia e di razza " + self.razza)
ilmiocane = cane(" ulysse ", " pastore tedesco ")
ilmiocane.abbaia()