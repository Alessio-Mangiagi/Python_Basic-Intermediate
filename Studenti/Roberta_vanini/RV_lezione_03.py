# Tipologie di elementi

lista = [1, 2, 3, 4] # Ordinata, permette duplicati, modificabile, indicizzabile.
tupla = (1, 2, 3, 4) # Ordinata, permette duplicati, NON modificabile, indicizzabile.
dizionario = {2:"a", 1:"b", 4:"c", 3:"d"} # NON ordinato, NON permette duplicati, modificabile, indicizzabile.
# ogni elemento di un dizionario è associato ad un indice.
# possiamo iterare un dizionario per creare un dataframe con pandas -> for key in dict:
set = {4, 9, 8, 2} # NON ordinato, NON permette duplicati, modificabile, NON indicizzabile.

print(f"set: {set} \nlista: {lista[0]} \ntupla: {tupla[0]} \ndizionario: {dizionario[1]}")
# possiamo richiamare il primo elemento per lista e tupla. I set non sono indicizabili. Il dizionario ha un suo indice.

# For loop: usando un range() itera una funzione che forniamo noi per i volte

studenti = ["Federico", "Gianluca", "Massimiliano", "Roberta", "Alessio", "Antonio", "Stefano", "Mauro",
            "Costanza", "Antonio", "Mariagiada", "Annalisa"]

# Il comando len() ci permette di contare elementi di una lista o lettere di una stringa. Comincia a contare da 1.

len("Roberta") # per una stringa ci ridà il numero di lettere
len(studenti) # per una lista ci fornisce il numero di elementi

# Se proviamo a dare len(10) ci dà errore perché i numeri non hanno len.
# Come facciamo a contare le cifre in un numero? Bisogna trasformarlo in stringa.

x = 238271.32
len(str(x))-1 # ATTENZIONE: ci da 9 perchè conta anche il punto

for i in range(len(studenti)):
    print("Studente numero", i + 1, ":", studenti[i])

# range con un salto di 2 posizioni

for i in range(0,10,2):
    print(i)

# partiamo dal 3o numero

for i in range(3,5):
    print(i)

# stampiano le lettere di una parola

parola = "Hello!"

for i in parola:
    print(i)

# stampiamo le lettere di una parola in ogni riga e dare un numero usiamo enumerate()

for indice, lettera in enumerate(parola):
    print(indice+1, lettera)        # indice+1 perché altrimenti comincia a contare da 0

###### CICLO WHILE: simile a for ma rimane attivo finché la condizione è vera
# PERICOLOSO perché potrebbe continuare a girare finché la macchina non crasha
# bisogna implementare delle condizioni di sicurezza per assicurarci che il ciclo si fermi.
# un cliclo while in loop infinito che effettua una chiamata ad un server può trasformarsi in un attacco DOS!

x = 0
while x in range(10):
    x = x+1
    print(x)

#########################################################
# 1. Esercizio: determinare se un numero è pari o dispari

def pari_dispari(num):
    """Inserisci il numero che vuoi controllare sia pari o dispari"""
    if num %2 == 0:
        print(f"{num} è pari.")
    else:
        print(f"{num} è dispari.")

#prova
pari_dispari(453535)

# 2. Esercizio: calcolo del massimo tra tre numeri

def max_tre(num1, num2, num3):
    """Inserisci i tre numeri che vuoi confrontare."""
    num_max = max(num1, num2, num3)
    print(f"Il numero più grande è: {num_max}")

max_tre(3,5,10)

# 3. Stampa dei primi N numeri (for loop)

def conta_fino(n):
    """Inserisci il numero intero fino a cui vuoi contare"""
    return range(n)

conta_fino(30)


# 4 Somma dei numeri da 1 a N con for

# 5. Uso del ciclo while per contare al contrario

# 6. Esercizio: tabellina del numero inserito

# 7. Ricerca in una lista: presenza elemento

# 8. Calcolo media e numero massimo da lista input

# 9. Contatore con ciclo e condizione

# 10. Esercizio: identificazione numeri primi

# 11. Stampa solo numeri pari da 1 a 100

# 12. Nested loop: tabella moltiplicazioni

# 13. Validazione input con while

# 14. Debugging: infinite loop e condizioni errate
