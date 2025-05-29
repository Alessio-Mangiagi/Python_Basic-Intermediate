## Controlli di WHILE
# Break: arresta la funzione

for x in range(10):
    if x == 5:
        break
    print(x)

# Continue: salta l'iterazione associata alla condizione fornita.

for x in range(5):
    x += 1
    if x == 3:
        continue
    print(x)


# Pass: passa al resto della funzione. Utile per debugging e far girare il codice prima di completarlo.

for x in range(5):
    x += 1
    print(x)
    if x > 3:
        pass #riempitivo per vedere se la funzione gira.

# Stampare una funzione?
import inspect

def conta_fino_10():
    for i in range(11):
        print(i)
    
print(conta_fino_10()) # python farà girare prima la funzione, poi printerà il valore: none (perchè non c'è return)
inspect.getsource(conta_fino_10) # per stampare il codice di una funzione serve la library inspect

studenti = ["Federico", "Gianluca", "Massimiliano", "Roberta", "Alessio", "Antonio", "Stefano", "Mauro",
            "Costanza", "Antonio", "Mariagiada", "Annalisa"]

#1. Scrittura di funzioni semplici (somma, fattoriale, media)
#2. Funzione per determinare se numero è pari o dispari
#3. Uso di return per inviare valore al chiamante
#4. Parametri con valori predefiniti
#5. Funzioni che accettano stringhe e restituiscono modifiche
#6. Funzione che calcola sconto su prezzo
#7. Creazione di un modulo personale utils.py
#8. Import di moduli math e random
#9. Simulazione di lancio dadi e generatore numeri casuali
#10. Import multiplo e alias
#11. Uso di variabili globali all’interno di funzione
#12. Test di funzioni con valori diversi
#13. Documentazione e help() su moduli
#14. Esercizio finale di refactoring con funzioni
#15. Preparazione a strutture dati