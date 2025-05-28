import math


print("Calcolo Area e Perimetro di un Rettangolo")
base = float(input("Dimmi la base del rettangolo: "))
altezza = float(input("Dimmi l'altezza del rettangolo: "))

#! FUNZIONE CHE RESTITUISCE L'AREA DI UN RETTANGOLO
def area_triangolo(base, altezza):
    return base * altezza

#! FUNZIONE CHE RESTITUISCE IL PERIMETRO DI UN RETTANGOLO
def perimetro_triangolo(base, altezza):
    return 2 * (base + altezza)

print("Area:", area_triangolo(base, altezza))
print("Perimetro:", perimetro_triangolo(base, altezza))


print("------------")


print("Calcolo Area e circonferenza di un cerchio")
raggio = float(input("Dimmi il raggio del cerchio: "))

#! FUNZIONE CHE RESTITUISCE L'AREA DI UN CERCHIO
def area_cerchio(raggio):
    return math.pi * raggio ** 2
#! FUNZIONE CHE RESTITUISCE LA CIRCONFERENZA DI UN CERCHIO
def circonferenza_cerchio(raggio):
    return 2 * math.pi * raggio

print("Area del cerchio:", area_cerchio(raggio))
print("Circonferenza del cerchio:", circonferenza_cerchio(raggio))


print("------------")


print("Area e Perimetro di un Triangolo")
base_triangolo = float(input("Dimmi la base del triangolo: "))
altezza_triangolo = float(input("Dimmi l'altezza del triangolo: "))
lato1 = float(input("Dimmi il primo lato del triangolo: "))
lato2 = float(input("Dimmi il secondo lato del triangolo: "))
lato3 = float(input("Dimmi il terzo lato del triangolo: "))

#! FUNZIONE CHE RESTITUISCE L'AREA DI UN TRIANGOLO
def area_triangolo(base, altezza):
    return (base * altezza) / 2
def perimetro_triangolo(base, altezza):
    # Perimetro del triangolo = somma dei tre lati
    return (lato1 + lato2 + lato3)
print("Area del triangolo:", area_triangolo(base_triangolo, altezza_triangolo))
print("Perimetro del triangolo:", perimetro_triangolo(base_triangolo, altezza_triangolo))