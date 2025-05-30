# studenti = ("Federico", "Marco", "Luca", "Giulia", "Sara")  #!lista, il conteggio parte da '0'
# for i in range(len(studenti)):
#     print(f"Studente {i + 1}: {studenti[i]}")  #!stampa il nome dello studente con il suo indice

#!len conta quanti elementi ci sono nella lista
#! range invece genera una sequenza di numeri da 0 al num

# print(list(range(6))) #!stampa i numeri da 0 a 5

# for i in range(0, 5, 2):  #!stampa i numeri da 0 a 4 con passo di 2
#     print(i)

# x = "ciao" #? stringa
# for i in range(0, len(x)):  #! range(start, stop)  #! length di x è 4, quindi stop è 4
#     print(x[i]) 




set = {1, 2, 3, 4, 5}  #!set di numeri, non ha duplicati e non ha indici
lista = [1, 2, 3, 4, 5]  #!lista di numeri
dizionario = {"nome": "Federico", "cognome": "Manni", "età": 70}  #!dizionario con chiavi e valori
tupla = ("Federico", "Manni", 25)  #!tupla con valori immutabili, sono tutte costanti
esimo = 0
print(f"set: {set}, Lista: {lista[esimo]}, Dizionario: {dizionario["nome"]}, Tupla: {tupla[esimo]}")