
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
                        try:
                            print(f"Risultato di {x} / {y} è: {round(x/y, 2)}")
                        except ZeroDivisionError:
                            print("Errore: Non si può dividere per 0")

                # Alla fine dell'operazione chiediamo se continuare o chiudere
                print("---------------------------------")
                continua = input("> Vuoi continuare a usare la Calcolatrice? (Yes/No) ")
                if continua.lower() == "yes":
                    return calcolatrice()
                else:
                    print("Grazie per aver usato la mia Calcolatrice! Arrivederci!\n")

# Proviamo!
calcolatrice()