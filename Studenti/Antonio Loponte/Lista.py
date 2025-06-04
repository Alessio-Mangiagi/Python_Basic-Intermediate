''' lista_persone = ["Luca", "Giada","Giorgio","Debora"]
print(lista_persone)
persona_nuova = input("Inserisci nome nuovo nome")

lista_persone.append(persona_nuova)
print(lista_persone)

lista_persone.insert(3,"Mattia") #il 3 è l'indice dove inserire il nome
print(lista_persone)

persona_trovata = lista_persone.pop(1)
print(lista_persone)

print(f"{persona_trovata} eccola")


print(lista_persone[3])

print(lista_persone[0:5:2]) #stampa da indice 0 a indice 5 a passi di 2


lista_persone.reverse()
print(lista_persone)  '''


# con i numeri

lista_numeri = [1,2,3,4]
print(lista_numeri)
numero_nuovo = input("Inserisci numero")

lista_numeri.append(numero_nuovo)
print(lista_numeri)

lista_numeri.insert(3,"46") #il 3 è l'indice dove inserire il nome
print(lista_numeri)

numero_trovato = lista_numeri.pop(4)
print(lista_numeri)

print(f"{numero_trovato} eccolo")


print(lista_numeri[3])

print(lista_numeri[0:5:2]) #stampa da indice 0 a indice 5 a passi di 2



''' lista_inversa = lista_numeri.copy()
lista_inversa.reverse()
lista =[lista_inversa]
print(sorted(lista)) '''

print(lista_numeri.count(3))

print(lista_numeri.index(2))


