def Saluti():
    print("Ciao, sono Alessio Mangiagi e questo è il mio toolbox!")
    print("Spero che ti piaccia!")
    print("Se hai bisogno di aiuto, non esitare a chiedere!")
    print("Buona giornata!")

def Somma(a, b):
    return a + b
def Somma_lista(lista):
    return sum(lista)
def Moltiplica(a, b):
    return a * b    
def Sottrai(a, b):
    return a - b
def Dividi(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    return a / b
def Potenza(base, esponente):
    return base ** esponente    
def RadiceQuadrata(numero):
    if numero < 0:
        return "Errore: radice quadrata di un numero negativo"
    return numero ** 0.5
def Fattoriale(n):
    if n < 0:
        return "Errore: fattoriale di un numero negativo"
    if n == 0 or n == 1:
        return 1
    risultato = 1
    for i in range(2, n + 1):
        risultato *= i
    return risultato
def CalcolaMedia(lista):
    if not lista:
        return "Errore: lista vuota"
    return sum(lista) / len(lista)
def TrovaMassimo(lista):
    if not lista:
        return "Errore: lista vuota"
    massimo = lista[0]
    for numero in lista:
        if numero > massimo:
            massimo = numero
    return massimo      
def TrovaMinimo(lista):
    if not lista:
        return "Errore: lista vuota"
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo   



def piramide():
    altezza =int(input("Inserisci l'altezza della pitamide: "))
    for i in range(1, altezza + 1):
        print(" " * (altezza - i) + "*" * (2 * i - 1))

def reversa_stringa(stringa):
    return stringa[::-1]    

def conta_vocali(stringa):
    vocali = str(input("Inserisci la parola: "))
    conteggio = 0
    for carattere in stringa:
        if carattere in vocali:
            conteggio += 1
    return conteggio

def che_giorno_è():
    import datetime
    giorno = datetime.datetime.now().strftime("%A")
    return f"Oggi è {giorno}"

def che_ora_è():
    import datetime
    ora = datetime.datetime.now().strftime("%H:%M:%S")
    return f"L'ora attuale è {ora}"