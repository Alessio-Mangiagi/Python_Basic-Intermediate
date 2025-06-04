class ContoBancario:
    def __init__(self, titolare, saldo):
        self.titolare = titolare
        self.__saldo = saldo
       
    def deposita(self, importo):
            self.__saldo += importo #attributo privato, incapsulato, non accessibile dall'esterno

    def preleva(self, importo):
        importo =
        if importo <= self.__saldo:
            self.__saldo -= importo
        else:
            raise ValueError("Saldo insufficiente per il prelievo.")

    def mostra_saldo(self):
        return self.__saldo
    
conto1 = ContoBancario("Stefano Moretti", 1000)
conto1.deposita(500)
print(conto1.mostra_saldo())  # Output: 1500
conto1.preleva(200)

    
    