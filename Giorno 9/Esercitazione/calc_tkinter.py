import tkinter as tk
from tkinter import ttk
from tkinter import Label, Entry, Button, LabelFrame

def calcolatrice():
    x = True
    while x:
        decisione = 0

        if decisione == "1":
            print("eseguo la somma")
            numero_1 = 0  
            numero_2 = 0 
            somma = float(numero_1) + float(numero_2)
            print(f"la somma è {somma}\n")   
        elif decisione == "2":
            print("eseguo la sottrazione")
            numero_1 = 0  
            numero_2 = 0 
            sottrazione = float(numero_1) - float(numero_2)
            print(f"la sottrazione è {sottrazione}\n")
        elif decisione == "3":
            print("eseguo la moltiplicazione")
            numero_1 = 0  
            numero_2 = 0 
            moltiplicazione = float(numero_1) * float(numero_2)
            print(f"la moltiplicazione è {moltiplicazione}\n")
        elif decisione == "4":
            print("eseguo la divisione")
            numero_1 = 0  
            numero_2 = 0
            try:
                divisione = float(numero_1) / float(numero_2)
                print(f"la divisione è {divisione}\n")
            except ZeroDivisionError:
                print("non si può inserire zero")
        else:
            print("il valore inserito non è riconosciuto")
        y = True
        while y:
            continua = 0
            if continua.lower() == 's':
                print("\n\n\n")
                y = False
            elif continua.lower() == 'n':
                x = False
                y = False
                print("Grazie per aver usato la calcolatrice!")
            else:
                print("Scusa non ho capito la tua scelta, riprova.")

#DA SISTEMARE

def addizione():
    schermata_addizione = tk.Tk()
    schermata_addizione.title("Click Counter")
    schermata_addizione.geometry("400x400")
    schermata_addizione.configure(bg="#1f1f1f")
    
    def somma():
        numero_1 = campo_1.get("1.0", tk.END)  
        numero_2 = campo_2.get("1.0", tk.END)
        somma = float(numero_1) + float(numero_2)
        label = tk.Label(schermata_addizione, text=f"la somma é {somma}")
        label.pack()
    
    # numero_1 = None  
    # numero_2 = None 
    numero_1 = campo_1.get("1.0", tk.END)  
    numero_2 = campo_2.get("1.0", tk.END)
    campo_1 = tk.Entry(schermata_addizione, width=50)
    campo_2 = tk.Entry(schermata_addizione, width=50)
    somma = float(numero_1) + float(numero_2)
    label = tk.Label(schermata_addizione, text=f"la somma é {somma}")
    campo_1.pack()
    campo_2.pack()
    label.pack()
    # somma()
def sottrazione():
    pass

def moltiplicazione():
    pass
    
def divisione():
    pass

root = tk.Tk()
root.title("Calcolatrice")
root.geometry("700x500")
root.configure(bg="#1f1f1f")

button_addizione = tk.Button(root, text="addizione", command=addizione)
button_addizione.pack()

button_sottrazione = tk.Button(root, text="sottrazione", command=sottrazione)
button_sottrazione.pack()

button_moltiplicazione = tk.Button(root, text="moltiplicazione", command=moltiplicazione)
button_moltiplicazione.pack()

button_divisione = tk.Button(root, text="divisione", command=divisione)
button_divisione.pack()

root.mainloop()