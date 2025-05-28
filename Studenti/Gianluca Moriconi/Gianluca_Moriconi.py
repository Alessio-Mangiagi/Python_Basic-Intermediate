#----------------------------------------------------------------------inizio funzione--------------------------------------------------------

def salutami(name): #definisco la funzione salutami, dichiarando la variabile name
    x ="ciao \n"    #definisco x
    y = name        #definisco y come valore preso da input
    frase = x + y   #definisco frase come somma dei valori di x e y
    print(frase)    #stampo frase

#----------------------------------------------------------------------fine funzione--------------------------------------------------------

name = input("inserisci il tuo nome:")  #richiede in input un valore string che finisce all'interno 

salutami(name)                          #richiamo la funzione salutami che prende il valore di Nome e lo trasferisce a name

if name == "gianluca":                  #creo un if con condizione name == gianluca
    print("come stai, capo?")           # se vero, stampo a schermo questo
elif name == "giuseppe":                #elif è alternativa ad else if. se invece name=giovanni stampo altro
    print("piacere rivederti!")
else:                                   #altrimenti in tutti gli altri casi faccio altro
    print("piacere di conoscerti!")

#--------------------------------------------------------------inizio funzione calcolatrice--------------------------------------------------------

def calcolatrice ():                                    #definisco la funzione calcolatrice
    print("Benvenuto nella calcolatrice!")              #stampo benvenuto
    n1 = float(input("inserisci il primo numero: "))    #prendo ad input un valore convertito in float e lo inserisco in n1
    n2 = float(input("inserisci il secondo numero: "))  #prendo ad input un valore convertito in float e lo inserisco in n2

    operazione = input("inserisci operazione:\n 1. Somma \n 2. Sottrazione \n 3. Moltiplicazione \n 4. Divisione \n") #inserisco una scelta in operazione
    if operazione == "1":                               #se operazione == 1
        somma(n1,n2)                                    # faccio somma
    elif operazione == "2":                             #se operazione == 2
        sottrazione(n1,n2)                              # faccio somma
    elif operazione == "3":                             #se operazione == 3
        moltiplicazione(n1,n2)                          # faccio somma
    elif operazione == "4":                             #se operazione == 4
        divisione(n1,n2)                                # faccio somma
    else:
        print("azz, c'è un errore")                     #se diverso, do messaggio

#--------------------------------------------------------------fine funzione calcolatrice--------------------------------------------------------

#----------------------------------------------------------------------inizio funzione somma--------------------------------------------------------

def somma(n1,n2):
    z = n1 + n2
    risultato = print (f"Il risultato è: {z}")
    return risultato                                    #restituisco il valore di risultato

#----------------------------------------------------------------------fine funzione somma--------------------------------------------------------

#----------------------------------------------------------------------inizio funzione sottrazione--------------------------------------------------------

def sottrazione(n1,n2):
    z = n1 - n2
    risultato = print (f"Il risultato è: {z}")
    return risultato

#----------------------------------------------------------------------fine funzione sottrazione--------------------------------------------------------

#----------------------------------------------------------------------inizio funzione moltiplicazione--------------------------------------------------------

def moltiplicazione(n1,n2):
    z = n1 * n2
    risultato = print (f"Il risultato è: {z}")
    return risultato

#----------------------------------------------------------------------fine funzione moltiplicazione--------------------------------------------------------

#----------------------------------------------------------------------inizio funzione divisione--------------------------------------------------------

def divisione(n1,n2):
    z = n1 / n2
    if n2 == 0:                                            #controllo divisibilità per 0
        risultato = print ("Il numero non può essere divisibile per 0")
    else:
        risultato = print (f"Il risultato è: {z}")
    return risultato
#----------------------------------------------------------------------fine funzione divisione--------------------------------------------------------

calcolatrice() #richiamo la funzione calcolatrice

print(f"questo è un altro modo di scrivere a schermo il risultato: {name}\n")
totale = name + " " + name
print(f"questo stampa due stringhe separate da spazi: {totale}\n")
print(f"questo è un altro modo che stampa due stringhe separate da spazi: {name} {name}\n")