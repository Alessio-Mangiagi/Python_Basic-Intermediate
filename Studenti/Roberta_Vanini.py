########## LEZIONE NUMERO 1 
print ("Hello World!")

x = "Hi everyone"
print (x)

y = "my name is Roberta"

print (x + " " + y)

## and if it was a number?

z = 33

# print (x + z)  # This will cause an error because you cannot concatenate a string and an integer directly
print (x + " " + str(z))  # Convert the integer to a string before concatenation

## funzione, va definita e poi "chiamata"

def function():
    print("This is a function")
function()

# creiamo una funzione per salutare qualcuno
def salutami(name):
    x = "Ciao "
    y = str(name) + "!"
    print(x + y)

name = input("Come ti chiami? ")
salutami(name)

# creiamo una funzione per salutare i colleghi
def saluta_colleghi(name):
    name = str(input("Come ti chiami? "))
    if name == "Roberta":
        print("Ehi capo! Come va?")
    elif name == "Giorgio":
        print("Bentornato Giorgio! Come stai?")
    elif name == "Simonetta":
        print("Ciao Mamma! Tutto bene?")
    else: print("Piacere di conoscerti! Benvenuto " + name + "!")

saluta_colleghi(name)

# creiamo funzione per calcolare area rettangolo

def area_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = base * altezza
    return area

area_rettangolo()

########## LEZIONE NUMERO 2

# creazione di una calcolatrice semplice

def calcolatrice():
    print("---------------------------------\nBenvenuto alla mia Calcolatrice!\n---------------------------------")
    print("Scegli un'operazione:\n 1. Addizione\n 2. Sottrazione\n 3. Moltiplicazione\n 4. Divisione\n 5. Esci")
    print("---------------------------------")

    # chiediamo di scegliere un'operazione
    scelta = input("> Seleziona l'operazione (1, 2, 3, 4, 5): ")
    operazioni = {
        '1': 'Addizione',
        '2': 'Sottrazione',
        '3': 'Moltiplicazione',
        '4': 'Divisione',
        '5': 'Esci'}
    
    # nel caso di operazione non valida (non presente tra le operazioni), richiediamo di ripetere la scelta
    if scelta not in operazioni: 
        print("Operazione non valida. Riprova.\n")
        return calcolatrice()
    
    # nel caso la scelta sia valida proseguiamo e chiediamo la conferma dell'operazione scelta
    else:
        print(f"\nHai scelto l'operazione: {operazioni.get(scelta)}")
        conferma = input("> è esatto? (Yes/No): ")

        # nel caso la risposta non sia "Yes" o "No", forniamo un messaggio di errore e richiediamo di ripetere la scelta
        if conferma.lower() != "yes" and conferma.lower() != "no":
            print("Errore: Risposta non valida.\nSi prega di rispondere con 'Yes' o 'No'.\n")
            return calcolatrice()  
        
        # nel caso la risposta è diversa da "Yes", annulliamo e richiediamo di ripetere la scelta
        elif conferma.lower() != "yes":
            print("Operazione annullata. Riprova.\n")
            return calcolatrice()  
        
        # nel caso la risposta sia "Yes", confermiamo e procediamo con l'operazione
        else:
            print("\nOperazione confermata.")

            # se l'operazione scelta è Esci, usciamo dalla calcolatrice
            if scelta == "5":
                print("Grazie per aver usato la mia Calcolatrice! Arrivederci!\n")

            # se l'operazione scelta esiste, chiediamo i numeri da calcolare e procediamo con l'operazione
            else:
                x = float(input("> Inserisci il primo numero: "))
                y = float(input("> Inserisci il secondo numero: "))
                print("---------------------------------")
                if scelta == "1":
                    print(f"Risultato di {x} + {y} è: {x+y}")
                elif scelta == "2":
                    print(f"Risultato di {x} - {y} è: {x-y}")
                elif scelta == "3":
                    print(f"Risultato di {x} * {y} è: {x*y}")
                elif scelta == "4":
                    if y == 0:
                        print("Errore: Divisione per zero non è permessa. Riprova.\n")
                        return calcolatrice()
                    else:
                        print(f"Risultato di {x} / {y} è: {round(x/y, 2)}")

                # Alla fine dell'operazione chiediamo se continuare o chiudere
                print("---------------------------------")
                continua = input("> Vuoi continuare a usare la Calcolatrice? (Yes/No) ")
                if continua.lower() == "yes":
                    return calcolatrice()
                else:
                    print("Grazie per aver usato la mia Calcolatrice! Arrivederci!\n")

# Proviamo!
calcolatrice()

########## LEZIONE NUMERO 3



########## LEZIONE NUMERO 4
########## LEZIONE NUMERO 5
########## LEZIONE NUMERO 6