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

def calcolatrice(): 
    print("Benvenuto")
    
   
    x = True

    numero_1 = input("dimmi il primo numero: ")  
    numero_2 = input("dimmi il secondo numero: ") 

    while x:
        decisione = input("Scegli un'operazione:\n(1) Somma\n)2) Sottrazione\n(3) Moltiplicazione\n(4) Divisione\n")

        if decisione == "1":
            print("eseguo la somma")
            
            somma = float(numero_1) + float(numero_2 )
            print(f"la somma è {somma}\n")   
        elif decisione == "2":
            print("eseguo la sottrazione")
            
            sottrazione = float(numero_1) - float(numero_2)
            print(f"la sottrazione è {sottrazione}\n")
        elif decisione == "3":
            print("eseguo la moltiplicazione")
           
            moltiplicazione = float(numero_1) * float(numero_2)
            print(f"la moltiplicazione è {moltiplicazione}\n")
        elif decisione == "4":
            print("eseguo la divisione")
            
            if numero_2 != "0":
                divisione = float(numero_1) / float(numero_2)
                print(f"la divisione è {divisione}\n")
            else:
                print("non si può inserire zero")
        else: 
            print("il valore inserito non è riconosciuto")
        y = continua
        while y:
            continua= input("Vuoi continuare? (si/no): ").lower()
            if continua.lower() == "si":
                print("\n\n\n\n\n\n\n\n\n")
                x = False  
                print("\n\n\n\n\n\n\n\n\n")
            elif continua.lower()== "no":
                x = False
                y = False
                print("\n\n\n\n\n\n\n\n\n")
                print("Grazie per aver usato la calcolatrice!") 
            else:
                x = False
                print("scusa non ho capito")
                