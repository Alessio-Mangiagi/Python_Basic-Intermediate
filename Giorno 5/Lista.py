lista_numeri = [0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5]
lista_studenti = ["Alice", "Zaza", "Bob", "Charlie", "Dave"]

#! AGGIUNTA ELEMENTI LISTA
# print(lista_numeri)
# lista_numeri.append(6)
# print(lista_numeri)
# lista_numeri.insert(7,8)
# print(lista_numeri)
# lista_numeri.extend([9, 10])
# print(lista_numeri)

#! RIMOZIONE ELEMENTI LISTA
# print(lista_numeri)
# print(lista_studenti)
# numero_rimosso = lista_numeri.remove(1)
# print(lista_numeri)
# numero_rimosso = lista_numeri.pop(0)
# studente_rimosso = lista_studenti.pop(2)
# print(lista_numeri)
# print(f"{numero_rimosso} e' stato rimosso")
# print(f"{studente_rimosso} e' stato rimosso")

#! ACCESSO E SLICING NELLA LISTA
# print(lista_numeri)
# print(lista_numeri[0])
# print(lista_numeri[0:6])
# print(lista_numeri[0:6:2])

#! METODI UTILI PER MANIPOLARE LE LISTE
# print(lista_studenti)
# lista_studenti.sort()           #? NON ASSOCIABILE A UNA VARIABILE, RITORNA None
# print(lista_studenti)
# lista_studenti_ordinata = sorted(lista_studenti)      #? ASSOCIABILE A UNA VARIABILE, RITORNA LISTA
# print(lista_studenti_ordinata)
# print(lista_studenti.sort())

lista_numeri_inversi = lista_numeri.copy()
lista_numeri_inversi.reverse()
# liste = [lista_numeri_inversi, lista_numeri]
# print(liste)
# print(sorted(liste))


# print(lista_numeri.count(2))

# print(lista_studenti.index("Alice"))
# print(lista_studenti.index("Charlie"))
# print(lista_numeri.index(2))

#! LIST COMPREHENSION
lista_potenza = [n**2 for n in lista_numeri] # list comprehension sintassi base
#print(lista_potenza)

lista_potenza_invertita = [i**2 for i in lista_numeri_inversi]
#print(lista_potenza_invertita)

lista_potenza = [n**2 for n in lista_numeri if n % 2 == 0] # filtri condizionali 
#print(lista_potenza)

listona_potenze = [lista_potenza for studente in lista_studenti] 
#print(listona_potenze) 

listona_potenze = [[n**2 for n in lista_numeri] for studente in lista_studenti]  
#print(listona_potenze)
 
# lista_potenza = [n**2 if n % 2 == 0 else print("numero dispari") for n in lista_numeri]
# print(lista_potenza)

listona_potenze_rev = [[i+n for i in lista_numeri_inversi] for n in lista_potenza] # list comprehension complessa 
print(listona_potenze_rev)

