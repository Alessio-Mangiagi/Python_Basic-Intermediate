# Lista

studenti = ["Federico", "Gianluca", "Massimiliano", "Roberta", "Alessio", "Antonio", "Stefano", "Mauro",
            "Costanza", "Antonio", "Mariagiada", "Annalisa"]

# 1. Esercizio: determinare se un numero è pari o dispari

def pari_dispari(num):
    """Inserisci il numero che vuoi controllare sia pari o dispari"""
    if num %2 == 0:
        print(f"{num} è pari.")
    else:
        print(f"{num} è dispari.")

#prova
pari_dispari(453535)

# 2. Esercizio: calcolo del massimo tra tre numeri

def max_tre(num1, num2, num3):
    """Inserisci i tre numeri che vuoi confrontare."""
    num_max = max(num1, num2, num3)
    print(f"Il numero più grande è: {num_max}")

max_tre(3,5,10)

# 3. Stampa dei primi N numeri (for loop)

def conta_fino(n):
    """Inserisci il numero intero fino a cui vuoi contare"""
    return range(n)

conta_fino(30)


# 4 Somma dei numeri da 1 a N con for

# 5. Uso del ciclo while per contare al contrario

# 6. Esercizio: tabellina del numero inserito

# 7. Ricerca in una lista: presenza elemento

# 8. Calcolo media e numero massimo da lista input

# 9. Contatore con ciclo e condizione

# 10. Esercizio: identificazione numeri primi

# 11. Stampa solo numeri pari da 1 a 100

# 12. Nested loop: tabella moltiplicazioni

# 13. Validazione input con while

# 14. Debugging: infinite loop e condizioni errate
