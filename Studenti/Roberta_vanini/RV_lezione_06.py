# Esercizi di ripasso lezione 5: liste
# Scrivi un programma in python che chiede all' utente di inserire 5 nomi
# (uno per volta) li memorizza in una lista e poi stampa tutti i nomi inseriti

lista_nomi = []

for n in range(5):
    nome = input(f"Inserisci il nome numero {n+1}: ")
    lista_nomi.append(nome)

print(lista_nomi)

# copia della lista chiamata numeri_miei 
# e aggiungiamo alal fine di numeri mie il numero 7
# inseriamo il numero 8 alla 3 posizione

lista_num = [1, 2, 3, 4, 5, 6]
numeri_miei = lista_num.copy()

numeri_miei.append(7)
print(numeri_miei)

numeri_miei.insert(2, 8)
print(numeri_miei)

# Rimuovi dalla lista numeri_miei la prima occorrenza del numero 8
# e estrai il primo nome e salviamolo e printiamo tutto

numeri_miei.remove(8)
print(numeri_miei)

primo_n = numeri_miei.pop(0)
print(primo_n)

## INIZIO LEZIONE 6
# Gestione dei File e Runtime

# open() interagisce con i file nella cartella
# file = open("dati.txt", r) apre in sola lettura
# file = open("output.tvt", w) crea nuovo file o sovrascrive
# file = open("log.txt", a) append, aggiunge contenuto a fine file
# file = open("nuovo.txt", x) exclusive creation, crea file ma non esegue se nome uguale per evitare sovrascritture

# file.read() legge tutto il contenuto come singola stringa
# file.readline() legge riga per riga, è più efficente di read()
# file.readlines() restituisce una lista di righe (stringhe)

# SCRITTURA FILE
# file.write() scrive una stringa nel file
# file.writelines() scrive sequenza stringhe nel file
# file.flush() forza la scrittura immediata dei dati nel file, svuotando buffer memoria interno

# apertura sicura: with da associare a open e altre operazioni
# with open("file.txt", "r") as f:
#    contenuto = file.read()

# codifica: usare encoding="utf-8"

# file.close() per chiudere le modifiche

with open("prova.txt", "w", encoding="utf-8") as f:
    f.write("Questo è un file di testo creato con python!\n")
    f.close()

# apriamo il file in modalità lettura

with open("prova.txt",  "r", encoding="utf-8") as f:
    contenuto = f.read() #leggiamo il contenuto
    print(contenuto) #stampiamo nel terminal
    f.close()

# aggiungiamo delle righe con una lista

righe = ["riga 1\n", "riga 2\n", "riga 3\n"]

with open("prova.txt", "a", encoding="utf-8") as f:
    f.write("Sto aggiungendo nuove righte\n")
    f.writelines(righe)
    f.flush() #svuota il buffer
    f.close()

# leggiamo nuovamente il file

with open("prova.txt",  "r", encoding="utf-8") as f:
    contenuto = f.read() #leggiamo il contenuto
    print(contenuto) #stampiamo nel terminal
    f.close()

# per i CSV bisogna importare la libreria csv
# writer fa parte della libreria csv
# creiamo un file csv

import csv

lista_righe= [["nome1", "cognome1", 1], ["nome2", "cognome2", 2], ["nome3", "cognome3", 3]]

with open(
    "Python_Basic-Intermediate/Studenti/Roberta_vanini/studenti.csv", "w", encoding= "utf-8", newline=""
    ) as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Cognome", "Età"]) #scriviamo l'header
    writer.writerow(["Roberta", "Vanini", "32"]) #scriviamo singola riga
    writer.writerows(lista_righe) #per aggiungere più righe in una volta
    f.close()

# vediamo il file

with open("Python_Basic-Intermediate/Studenti/Roberta_vanini/studenti.csv", "r", encoding= "utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for riga in reader:
        print(riga["Nome"])
    f.close()

# GESTIONE DEGLI ERRORI: Introduzione eccezioni Try/Except
# try contiene codice potenzialmente problematico
# except definisce azioni da eseguire quando si verifica un'eccezione

try:
    risultato = 10/0
except ZeroDivisionError:
    print("Impossibile dividere per zero")
    risultato = 0

# si possono creare più eccezioni, scrivendo except con il tipo di errore specifico
# nel caso di errore imprevisto

try:
    file = open("dati.txt", "r")
    numero = int(file.readline())
    risultato = 100/numero
except Exception as e:
    print(f"Errore imprevisto {e}")

# Cosa fare?
# Specificità: Andare a prendere in considerazione eccezioni specifiche
# Logging: Registra errori significativi con dettagli per debugging futuro
# Recovery: Implementa strategie per recupero quando possibile, fornendo valori o operazioni alternative
# User experience: Messaggi comprensibili agli utenti anche non tecnici