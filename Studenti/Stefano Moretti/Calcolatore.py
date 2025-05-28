# Creiamo le funzioni delle aree delle figure geometriche
def area_rettangolo(base, altezza):
    return base * altezza

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_cerchio(raggio):
    return 3.14 * (raggio ** 2)

def area_trapezio(base_1, base_2, altezza):
    return ((base_1 + base_2) * altezza) / 2

# Creiamo l'inizio del nostro calcolatore aree
def area_geometrica():
    print("Benvenuto nel calcolatore di aree!")
    figura = input("Che tipo di area vorresti calcolare? Seleziona il numero in base alla figura geometrica:\n1. rettangolo\n2. triangolo\n3. cerchio\n4. trapezio\noppure digita 'exit' per uscire: ")
    if figura == "exit":
        print("Chiusura del programma, alla prossima!")
        
    
    # Chiediamo all'utente di inserire i dati in base alla figura scelta
    if figura in ["1", "2"]:
        base = float(input("Per favore, inserisci la base: "))
        altezza = float(input("E adesso l'altezza: "))
    elif figura == "3":
        raggio = float(input("Per favore, inserisci il raggio: "))
    elif figura == "4": 
        base_1 = float(input("Per favore, inserisci la prima base: "))
        base_2 = float(input("E adesso la seconda base: "))
        altezza = float(input("E adesso l'altezza: "))
    else:
        print("Ehm... Hai sbagliato qualcosa!")
        

    # Eseguiamo il calcolo dell'area in base alla figura scelta
    if figura == "1":
        print(f"L'area del rettangolo è: {area_rettangolo(base, altezza)}") 
    elif figura == "2":
        print(f"L'area del triangolo è: {area_triangolo(base, altezza)}")
    elif figura == "3":
        print(f"L'area del cerchio è: {area_cerchio(raggio)}")
    elif figura == "4":
        print(f"L'area del trapezio è: {area_trapezio(base_1, base_2, altezza)}")
    else:
        print("Ehm... Hai sbagliato qualcosa!")


# Creiamo le varie funzioni somma, sottrazione, moltiplicazione, divisione, potenza e radice quadrata
def somma(x, y):
    return x + y

def sottrazione(x, y):
    return x - y

def moltiplicazione(x, y):
    return x * y

def divisione(x, y):
    if y == 0:
        return "Errore: Non possiamo dividere per 0."
    return x / y

def potenza(x, y):
    return x ** y

def radice_quadrata(x):
    if x < 0:
        return "Errore: Radice quadrata di un numero negativo non permessa."
    return x ** 0.5
    
def radice_cubica(x):
        if x < 0:
            return -(-x) ** (1/3)
        return x ** (1/3)

# Creiamo la funzione calcolatrice
def calcolatrice():
    segno = input("Inserisci il segno dell'operazione:\n+. per la somma\n-. per la sottrazione\n*. per la moltiplicazione\n/. per la divisione\n^. per la potenza\nV2. per la radice quadrata (Ricorda, non puoi inserire numeri negativi)\nV3. per radice cubica (Ricorda, non puoi inserire numeri negativi)\noppure se vuoi uscire digita 'exit' per uscire: ") 
    if segno == "exit":
        print("Chiusura della calcolatrice, alla prossima!")
        
    
    # Chiediamo all'utente di inserire i numeri e chiediamo y solo se non è una radice    
    x = float(input("Inserisci il primo numero: "))
    if segno == "V2":
        print(f"La radice quadrata di {x} è: {radice_quadrata(x)}")
    elif segno == "V3":
        print(f"La radice cubica di {x} è: {radice_cubica(x)}")
    else:
        y = float(input("Inserisci il secondo numero: "))

    # Creiamo la logica della nostra calcolatrice
    if segno == '+':
        print(f"Il risultato della somma è: {somma(x, y)}")
    elif segno == '-':
        print(f"Il risultato della sottrazione è: {sottrazione(x, y)}")
    elif segno == '*':
        print(f"Il risultato della moltiplicazione è: {moltiplicazione(x, y)}")
    elif segno == '/':
        print(f"Il risultato della divisione è: {divisione(x, y)}")
    elif segno == '^':
        print(f"Il risultato della potenza è: {potenza(x, y)}")
    else:
        print("Ehm... Hai sbagliato qualcosa!")

# Creiamo una funzione per il convertitore di temperatura
def conv_temperatura():
    print("Benvenuto nel convertitore di temperatura!")
    conversione = input("Come vuoi convertire la temperatura? Digita: \nC. da Celsius a Fahrenheit \nF. da Fahrenheit a Celsius \noppure 'exit' per uscire: ").strip().upper()
    if conversione == 'exit':
        print("Chiusura del convertitore, alla prossima!")
    elif conversione == 'C':
        celsius = float(input("Inserisci la temperatura in gradi Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura in Fahrenheit è: {fahrenheit}°F")
    elif conversione == 'F':
        fahrenheit = float(input("Inserisci la temperatura in gradi Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"La temperatura in Celsius è: {celsius}°C")
    else:
        print("Ehm... Hai sbagliato qualcosa!")

# Creiamo il nostro calcolatore
def calcolatore():
    print("Benvenuto nel calcolatore!")
    tipo_calcolo = input("Vorresti eseguire una semplice operazione aritmetica o calcolare l'area di una figura geometrica? Digita:\n1. per operazione aritmetica\n2. per calcolo area figura geometrica\n3. per conversione di temperature\noppure digita 'exit' per uscire: ")
    if tipo_calcolo == "exit":
        print("Chiusura del programma, alla prossima!")
    elif tipo_calcolo == "1":
        calcolatrice()
    elif tipo_calcolo == "2":
        area_geometrica()
    elif tipo_calcolo == "3":
        conv_temperatura()
    else:   
        print("Ehm... Hai sbagliato qualcosa!")
         

    
calcolatore()
  




