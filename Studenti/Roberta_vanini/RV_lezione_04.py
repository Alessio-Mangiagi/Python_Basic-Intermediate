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

def somma(n1, n2):
    """Funzione per sommare due numeri. Accetta valori int e float."""
    sum = n1 + n2
    return sum

somma(1,3)

def fattoriale(n):
    """Funzione per calcolare il fattoriale di un numero.\n
    Accetta valori int e float.\n
    La formula di un fattoriale è: n! = 1\*2\*...\*n\n
    Il fattoriale di 0 = 1"""
    if n == 0:
        return 1
    for i in range(1, n+1):
        fattoriale *= i
    return fattoriale

fattoriale(4)

def media(lista):
    """Funzione per calcolare la media di una lista di numeri.\n
    La formula della media è: (x1\+x2\+...\+xn)/n\n
    Fornire una lista vuota restituirà errore."""
    if not lista:
        print("La lista fornita è vuota.\nCrea una lista di numeri di cui vuoi calcolare la media.")
        return None
    somma = 0
    for valore in lista:
        somma += valore
    return somma / len(lista)
    
lista = [1,2.3,3.2,4.9,5]
media(lista) 

#2. Funzione per determinare se numero è pari o dispari

def pari_o_dispari(n):
    """Funzione per vedere se una variabile è pari o dispari.
    La variabile deve essere un intero o float."""
    if n%2 == 0:
        print(f"Il numero {n} è pari")
    elif n%2 == 1:
        print(f"Il numero {n} è dispari")
    else:
        print(f"Errore. Fornisci un numero.")

pari_o_dispari(2321)

#3. Funzione che calcola sconto su prezzo

def prezzo_scontato(prezzo, percent):
    """La funzione serve a calcolare il nuovo prezzo scontato.\n
    Le variabili sono: - Prezzo: il prezzo intero. (int, float)\n
                       - Percent: la percentuale di sconto. (int, float)\n"""
    sconto = (percent*prezzo)/100
    new_prezzo = prezzo - sconto
    return round(new_prezzo, 2)

prezzo_scontato(37.5, 25)

#4. Simulazione di lancio dadi e generatore numeri casuali

import random

def lancio_dadi(n, facce):
    """Lancia i dadi n volte.\n
    Le variabili sono:  - n: il numero di volte che viene lanciato il dado.\n
                        - facce: numero di facce del dado. 
                            Valori consigliati: 4, 6, 8, 10, 20, 100."""
    risultati = []
    for i in range(1, n+1):
        roll = random.randint(1, facce)
        risultati.append(roll)
        print(f"Lancio numero: {i}, risultato: {roll}")
    return print(f"La media dei lanci è: {round(media(risultati),2)}")

lancio_dadi(4,20)

#5. Esercizio finale di refactoring con funzioni
