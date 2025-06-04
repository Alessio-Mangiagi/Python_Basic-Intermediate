import csv
with open("Python_Basic-Intermediate\\Studenti\\Stefano Moretti\\Esercizi\\20240904_183206_export.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)
