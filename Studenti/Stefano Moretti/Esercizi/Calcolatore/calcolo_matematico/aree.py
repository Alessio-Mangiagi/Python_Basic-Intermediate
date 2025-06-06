

# Funzioni per il calcolo delle aree di diverse figure geometriche
def area_rettangolo(base, altezza):
    return base * altezza

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_cerchio(raggio):
    return 3.14 * (raggio ** 2)

def area_trapezio(base_1, base_2, altezza):
    return ((base_1 + base_2) * altezza) / 2

# Funzione del calcola aree
def calcola_area():
    print("Benvenuto nel calcolatore di aree!")
    x = True
    while x:
        figura = str(input("Digita un numero in base alla figura interessata, altrimenti digita 'exit':\n1. rettangolo\n2. triangolo\n3. cerchio\n4. trapezio: "))
        if figura == "exit":
            print("Chiusura del programma, alla prossima!")
            x = False
            break
        elif figura in ["1", "2"]:
            base = float(input("Per favore, inserisci la base: "))
            altezza = float(input("E adesso l'altezza: "))
            if figura == "1":
                print(f"L'area del rettangolo è: {area_rettangolo(base, altezza)}")
            elif figura == "2":
                print(f"L'area del triangolo è: {area_triangolo(base, altezza)}")
        elif figura == "3":
            raggio = float(input("Per favore, inserisci il raggio: "))
            print(f"L'area del cerchio è: {area_cerchio(raggio)}")
        elif figura == "4":
            base_1 = float(input("Per favore, inserisci la prima base: "))
            base_2 = float(input("E adesso la seconda base: "))
            altezza = float(input("E adesso l'altezza: "))
            print(f"L'area del trapezio è: {area_trapezio(base_1, base_2, altezza)}")
        else:
            print("Ehm... Hai sbagliato qualcosa!")
            continue

calcola_area()

        



