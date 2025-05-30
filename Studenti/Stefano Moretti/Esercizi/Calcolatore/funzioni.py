# Funzioni del calcolatore

# Creiamo le funzioni delle aree delle figure geometriche
def area_rettangolo(base, altezza):
    return base * altezza

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_cerchio(raggio):
    return 3.14 * (raggio ** 2)

def area_trapezio(base_1, base_2, altezza):
    return ((base_1 + base_2) * altezza) / 2