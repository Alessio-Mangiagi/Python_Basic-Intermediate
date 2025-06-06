with open(
    "file.txt", "w", encoding="utf-8"
) as f:  # Apriamo il file in modalità di scritttura ("w") e con codifica utf-8
    f.write("Ciao, questo è un file di testo.\n")
    f.close()

righe = [
    "ecco la riga1 di prova\n",
    "ecco la riga2 di prova\n",
    "ecco la riga3 di prova\n",
]

with open(
    "file.txt", "a", encoding="utf-8"
) as f:  # Apriamo il file in modalità di aggiunta ("a")
    f.write("Aggiungiamo una nuova riga al file.\n")
    f.writelines(righe)
    f.flush()  # Forziamo la scrittura su disco

    f.close()

count = 0
with open(
    "file.txt", "r", encoding="utf-8"
) as f:  # Apriamo il file in modalità di lettura ("r")
    contenuto = f.read()  # Leggiamo tutto il contenuto del file
    # righelista = (
    #   f.readlines()
    # )  # Leggiamo il file riga per riga e le mettiamo in una lista
    print(contenuto)  # Stampiamo il contenuto del file
    # print(righelista)  # Stampiamo la lista delle righe lette

    # print(f.readline())  # Leggiamo una riga alla volta e stampiamo il numero di riga

    f.close()  # Chiudiamo il file


import csv

with open(
    "Studenti\\Alessio Mangiagi\\20240904_183206_export.csv", "r", encoding="utf-8"
) as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)


lista = [
    ["Giulia", "Neri", 28],
    ["Luca", "Bianchi", 32],
    ["Sara", "Verdi", 27],
]

with open("studenti.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Cognome", "Età"])
    writer.writerow(["Mario", "Rossi", 25])
    writer.writerows(lista)
    writer.writerow(["Luigi", "Bianchi", 30])
    writer.writerow(["Anna", "Verdi", 22])
