# controllo numeri pari e dispari

numero = input("Inserisci un numero per verificare se è pari o dispari: ")

def pari_dispari(numero):
    if int(numero) % 2 == 0:
        print(f"{numero} è un numero pari.")
    else:
        print(f"{numero} è un numero dispari.") 

pari_dispari(numero)
