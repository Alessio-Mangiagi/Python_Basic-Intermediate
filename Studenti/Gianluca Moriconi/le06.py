#esercizio 1
"""
lista_nomi = []

def ins_nomi():
    for i in range(5):
        nome = input("Inserisci un nome: ")
        lista_nomi.append(nome)
    
ins_nomi()
print(lista_nomi)

nomi_miei = lista_nomi.copy()

nomi_miei.append("Gianluca")
nomi_miei.insert(2, "Luca")
print(nomi_miei)

nomi_miei.remove("Luca")
print(nomi_miei)

nome_tolto = nomi_miei.pop(0)
print(f"Il nome tolto è: {nome_tolto}")
"""

# ----------------------------------------------------operazioni con file------------------------------------------
"""
with open("file.txt", "w", encoding="utf-8") as file:               #apre il file in modalità scrittura, se non esiste lo crea, con codifica utf-8 
    file.write("Ciao, questo è un file di testo.\n")                #scrive una riga nel file
    file.close()                                                    #chiude il file, ma non è necessario in questo caso perché il blocco with lo chiude automaticamente

righe= ["Prima riga del file.\n", "Seconda riga del file.\n", "Terza riga del file.\n"]

with open("file.txt", "a", encoding="utf-8") as file:               #apre il file in modalità append, per aggiungere contenuto senza sovrascrivere
    file.write("Aggiungo un'altra riga al file.\n")  
    file.writelines(righe)                                          #aggiunge più righe al file
    file.flush()                                                    #forza la scrittura su disco, ma non è necessario in questo caso perché il blocco with lo fa automaticamente
    
    file.close()  

with open("file.txt", "r", encoding="utf-8") as file:               #apre il file in modalità lettura
    
    contenuto = file.read()                                         #legge tutto il contenuto del file
    #righelista = (file.readlines())                                #legge il file riga per riga e le mette in una lista
    
    print(contenuto)                                                #stampa il contenuto del file
    #print(righelista)                                              #stampa la lista delle righe lette

    #print(file.readline())                                         #legge e stampa la prima riga del file
    
    file.close()  
"""
#-----------------------------------------------------

import csv                                                          # Importa il modulo csv per lavorare con i file CSV

"""
listastud_01 = [["Gianluca", "Neri", 33], 
                ["Luca", "Rossi", 30],
                ["Anna", "Bianchi", 22]] 


with open("studenti.csv", "w", encoding="utf-8", newline="") as file: 
    writer = csv.writer(file)                                       # Crea un oggetto writer per scrivere nel file CSV       
    writer.writerow(["Nome", "Cognome", "Età"])                     # Passa una lista, non una stringa
    writer.writerow(["Gianluca", "Moriconi", 25])
    writer.writerow(["Luca", "Rossi", 30])
    writer.writerow(["Anna", "Bianchi", 22])
    writer.writerows(listastud_01)                                  # Scrive le righe della lista nel CSV

with open("studenti.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)                                       # Crea un oggetto reader per leggere dal file CSV
    for row in reader:                                              # Itera su ogni riga del file CSV
        print(row)                                                  # Stampa la riga corrente
"""
#------------------------------------------------------
"""
with open("studenti.csv", "w", encoding="utf-8", newline="") as file: 
    writer = csv.writer(file)                                       # Crea un oggetto writer per scrivere nel file CSV       
    writer.writerow(["Nome", "Cognome", "Età"])                         
    writer.writerow(["Gianluca", "Moriconi", 25])   
    writer.writerow(["Luca", "Rossi", 30])
    writer.writerow(["Anna", "Bianchi", 22])

with open("studenti.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)                                  # Crea un oggetto DictReader per leggere il file CSV come dizionari
    for rigadict in reader:     
        print(rigadict)                                            # Stampa ogni riga come un dizionario
"""
#------------------------------------------------------

