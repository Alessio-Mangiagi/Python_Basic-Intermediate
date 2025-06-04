def rettangolo ():
    base = float(input("inserisci la base del rettangolo:"))
    altezza = float(input("inserisci l'altezza del rettangolo:"))
    area = base * altezza
    perimetro = 2 * (base + altezza)
    print(f"l'area del rettangolo è: {area}")
    print(f"il perimetro del rettangolo è: {perimetro}")

rettangolo()



def cerchio() :
    raggio = float(input("inserisci il raggio del cerchio:"))
    area = 3.14 * (raggio ** 2)
    circonferenza = 2 * 3.14 * raggio
    print(f"l'area del cerchio è: {area}")
    print(f"la circonferenza del cerchio è: {circonferenza}")

cerchio()




def triangolo():
    base = float(input("inserisci la base del triangolo:"))
    altezza = float(input("inserisci l'altezza del triangolo:"))
    area = (base * altezza) / 2
    perimetro = base + altezza + (base ** 2 + altezza ** 2) ** 0.5  # approssimazione per il terzo lato
    print(f"l'area del triangolo è: {area}")
    print(f"il perimetro del triangolo è: {perimetro}")

triangolo()


def avvia_programma() :
    print("Scegli una figura geometrica:")
    print("1. Rettangolo")
    print("2. Cerchio")
    print("3. Triangolo")
    
    scelta = input("Inserisci il numero della figura: ")
    
    if scelta == "1":
        rettangolo()
    elif scelta == "2":
        cerchio()
    elif scelta == "3":
        triangolo()
    else:
        print("Scelta non valida. Riprova.")

avvia_programma()