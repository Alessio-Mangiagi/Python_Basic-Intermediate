studenti = ["giuseppe", "gianluca", "francesco","costanza"]
for i in range (len(studenti)):
    print("Studente numero", i + 1, ":", studenti[i]) # si aumenta il counter i a +1 per non partire da zero
  
  
"""
x = 570 #viene considerato intero
y = str(x) #viene considerato stringa
for i in range (len(y)): #len() calcola il numero di valori che compongono la variabile
    print(i) #stampa indice di ciclo
""" 

x = "570000" #stinga
for i in range (0, len(x)):  #range(start,stop)
    print(i)
#---------------------------------------------------------------------------------------------------------------
    
set = {1, 8, 7, 4} #insieme di numeri - collezione non ordinata di elementi unici
lista = [1,2,3,4] #esempio di lista - sequenza ordinata e modificabile di elementi
tupla = (1,2,3,4) #esempio di tupla - sequenza ordinata e immutabile di elementi
dizionario = {"nome": "alessio", "cognome": "mangiagi", "eta": 27} #esempio di dizionario - collezione di coppie chiave-valore
esimo = 0

print(f" set: {set} \n lista: {lista[esimo]}, \n tupla: {tupla[esimo]}\n dizionario: {dizionario['nome']} \n" )

#----------------------------------------------------------------------------------------------------------------

