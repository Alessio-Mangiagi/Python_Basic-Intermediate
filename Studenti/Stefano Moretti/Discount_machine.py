def sconto():
    print("Benvenuto nel calcolatore di sconti!")
    while True:
        risposta = input("Vuoi calcolare uno sconto? (s/n): ").strip().lower()
        if risposta == "s":
            try:
                prezzo = float(input("Inserisci il prezzo del prodotto: "))
                if prezzo < 0:
                    print("Il prezzo non può essere negativo.")
                    continue
                sconto = float(input("Inserisci la percentuale di sconto: "))
                if not (0 <= sconto <= 100):
                    print("La percentuale di sconto deve essere tra 0 e 100.")
                    continue
                prezzo_scontato = prezzo * (1 - sconto / 100)
                print(f"Il prezzo scontato è: {prezzo_scontato:.2f} euro")
            except ValueError:
                print("Per favore inserisci un valore numerico valido.")
        elif risposta == 'n':
            print("Grazie per aver utilizzato il calcolatore di sconti!")
            break
        else:
            print("Risposta non valida. Per favore, rispondi con 's' o 'n'.")

sconto()