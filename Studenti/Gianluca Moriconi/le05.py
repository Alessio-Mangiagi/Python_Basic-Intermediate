Studenti = ['Gianluca', 'Mario', 'Luca', 'Giovanni', 'Marco']
Numeri = [1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]



Studenti.append('Gianni')                   #inserisce Gianni alla fine della lista (un solo elemento)
print(Studenti)
Studenti.insert(2, 'Francesco')             #inserisce Francesco alla posizione 2 della lista
print(Studenti)
Studenti.extend(['Alessandro', 'Matteo'])   #estende la lista alla fine con Alessandro e Matteo (più elementi)
print(Studenti)
Studenti.remove('Giovanni')                 #rimuove Giovanni dalla lista
print(Studenti)
Numero_tolto = Studenti.pop(3)              #rimuove ma restituisce l'elemento alla posizione 3 della lista (solo un elemento)
print(Studenti)
print(f"Elemento rimosso: {Numero_tolto}")
#Studenti.clear() #svuota la lista
#print(Studenti)

"""
#-------------------------------------------Accesso e slicing degli elementi della lista--------------------------------------------

print(Studenti[0])                          #stampa il primo elemento della lista
print(Studenti[0:6])                        #stampa gli elementi dalla posizione 0 alla 5 (6 escluso)
print(Studenti[0:6:2])                      #stampa gli elementi dalla posizione 0 alla 5 con passo 2 (ogni secondo elemento)

#-------------------------------------------Metodi utili per manipolare le liste----------------------------------------------------

Studenti.sort()                             #ordina la lista in ordine alfabetico (numerico per i numeri)
#print(Studenti)
Studenti_ordered = sorted(Studenti)         #ordina la lista in ordine alfabetico (numerico per i numeri) e restituisce una nuova lista
#print(Studenti_ordered)

Numeri_rev = Numeri.copy()                  #crea una copia della lista Numeri 
                                            #IMPORTANTE: se non si usa copy(), la lista Numeri_rev punterebbe alla stessa lista di Numeri
Numeri_rev.reverse()                        #inverte l'ordine degli elementi della lista
print(Numeri)

liste = [Numeri_rev, Numeri]                #crea una lista di liste
print(liste)                                #stampa la lista di liste
print(sorted(liste))                        #ordina le liste in base al primo elemento di ogni lista

#-------------------------------------------Contare gli elementi di una lista----------------------------------------------------

x = input("Inserisci il numero che vuoi contare: ")
numero_di_{x} = Numeri.count(int(x))  #conta il numero di volte che x appare nella lista Numeri 

contatori = {} #crea un dizionario per contare gli elementi della lista Numeri
contatori [f"Numero di {x}"] = Numeri.count(int(x)) if x.isdigit() else Numeri.count(x)  #conta il numero di volte che x appare nella lista Numeri e lo aggiunge al dizionario contatori
print(contatori) 



print(Numeri.count(2))  #conta il numero di volte che 2 appare nella lista Numeri
print(Numeri.index(2))   #restituisce la posizione del primo elemento 2 nella lista Numeri
"""

#-------------------------------------------Esempio di list cromprehension-------------------------------------------------------

lista_potenza = [n**2 for n in Numeri] #crea una lista dei quadrati dei numeri della lista Numeri
print(lista_potenza)  #stampa la lista dei quadrati dei numeri della lista Numeri

#-------------------------------------------Esempio di list cromprehension con condizione----------------------------------------

lista_potenza_cond = [n**2 for n in Numeri if n % 2 == 0]  #crea una lista dei quadrati dei numeri della lista Numeri solo se il numero è pari
print(lista_potenza_cond)  