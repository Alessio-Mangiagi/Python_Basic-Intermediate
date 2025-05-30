lista_numeri = [0, 1, 2, 3, 4, 5]

lista_numeri_inversi = lista_numeri.copy() # crea una copia della lista per non modificare l'originale
lista_numeri_inversi.reverse() # inverte l'ordine degli elementi della lista

listona_rev = [[i+n for i in lista_numeri_inversi] for n in lista_numeri] # list comprehension complessa 
print(listona_rev) 