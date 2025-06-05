Stanze = ["Cucina", "Soggiorno", "Camera da letto", "Bagno", "Studio"] # lista di stanze
tre_prese = [s for s in Stanze if len(s) <= 5] # list comprehension per filtrare le stanze con nome di 5 o meno caratteri
quattro_prese = [s for s in Stanze if len(s) == 6] # list comprehension per filtrare le stanze con nome di più di 5 caratteri
cinque_prese = [s for s in Stanze if len(s) >= 6] # list comprehension per filtrare le stanze con nome di 5 o più caratteri
list_c = [tre_prese, quattro_prese, cinque_prese] # lista di liste con le stanze filtrate
list = [p for p in list_c ]
print(list) # stampa la lista di liste con le stanze filtrate

