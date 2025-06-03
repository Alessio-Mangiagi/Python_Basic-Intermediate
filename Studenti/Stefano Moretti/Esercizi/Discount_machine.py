def sconto():
    print("Benvenuto nel calcolatore di sconti!")
    x = True
    while x:   
        prezzo = input("Inserisci il prezzo del prodotto o digita 'exit' per uscire: ")
        if prezzo.lower() == "exit":
            print("Chiusura del programma, alla prossima!")
            x = False
            break
        try:
            prezzo_fl = float(prezzo)
            if prezzo_fl < 0:
                raise ValueError("Il prezzo non può essere negativo.") 
        except ValueError as e:
            print(f"Errore: {e}. Per favore, inserisci un prezzo valido.")
            continue

        sconto_percentuale = float(input("Inserisci la percentuale di sconto: "))
        if sconto_percentuale == "exit":
            print("Chiusura del programma, alla prossima!")
            x = False
            break
        
        sconto_calcolato = prezzo_fl * (sconto_percentuale / 100)
        prezzo_finale = prezzo_fl - sconto_calcolato
        
        print(f"Il prezzo finale dopo uno sconto del {sconto_percentuale}% è: {prezzo_finale:.2f}€")

sconto()