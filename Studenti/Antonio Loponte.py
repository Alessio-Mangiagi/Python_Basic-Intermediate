# calcolatrice con funzioni


print("benvenuto nella calcolatrice")
numero_uno = int(input("Inserisci il primo numero: "))
numero_due = int(input("Inserisci il secondo numero: "))
print("Scegli l'operazione da eseguire:\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione")
numero_operazione = input("Inserisci il numero dell'operazione: ")
print(f"Hai scelto l'operazione numero: {numero_operazione}")

def calcolatrice(numero_uno, numero_due,numero_operazione):
    if numero_operazione == "1":
        risultato = int(numero_uno) + int(numero_due)
        print(f"La somma di {numero_uno} e {numero_due} è: {risultato}")
    elif numero_operazione == "2":
        risultato = int(numero_uno) - int(numero_due)
        print(f"La sottrazione di {numero_uno} e {numero_due} è: {risultato}")
    elif numero_operazione == "3":
        risultato = int(numero_uno) * int(numero_due)
        print(f"La moltiplicazione di {numero_uno} e {numero_due} è: {risultato}")
    elif numero_operazione == "4":
        if int(numero_due) != 0:
            risultato = int(numero_uno) / int(numero_due)
            print(f"La divisione di {numero_uno} e {numero_due} è: {risultato}")
        else:
            print("Errore: Divisione per zero non consentita.")
    else:
        print("Operazione non valida.")


calcolatrice(numero_uno, numero_due, numero_operazione)


