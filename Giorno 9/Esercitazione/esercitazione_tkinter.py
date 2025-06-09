import tkinter as tk


def finestra_operazione(operazione):
    finestra = tk.Toplevel()
    finestra.title(f"Calcolatrice - {operazione}")
    finestra.geometry("400x400")

    tk.Label(finestra, text="Primo numero:").pack()
    primo_numero = tk.Entry(finestra, width=22)
    primo_numero.pack()
    tk.Label(finestra, text="Secondo numero:").pack()
    secondo_numero = tk.Entry(finestra, width=22)
    secondo_numero.pack()

    risultato_label = tk.Label(finestra, text="Risultato: ")
    risultato_label.pack()

    def calcola():
        try:
            num1 = float(primo_numero.get())
            num2 = float(secondo_numero.get())
            if operazione == "Addizione":
                risultato = num1 + num2
            elif operazione == "Sottrazione":
                risultato = num1 - num2
            elif operazione == "Moltiplicazione":
                risultato = num1 * num2
            elif operazione == "Divisione":
                if num2 == 0:
                    risultato_label.config(text="Errore: Divisione per zero")
                    return
                risultato = num1 / num2
            risultato_label.config(text=f"Risultato: {risultato}")
        except ValueError:
            risultato_label.config(text="Errore: Inserisci numeri validi")

    tk.Button(finestra, text="Calcola", command=calcola).pack()
    tk.Button(finestra, text="Chiudi", command=finestra.destroy).pack()


def addizione():
    finestra_operazione("Addizione")


def sottrazione():
    finestra_operazione("Sottrazione")


def moltiplicazione():
    finestra_operazione("Moltiplicazione")


def divisione():
    finestra_operazione("Divisione")


root = tk.Tk()
root.title("Calcolatrice")
root.geometry("300x300")
tk.Label(text="Scegli un'operazione:").pack()
tk.Button(root, text="Addizione", command=addizione).pack()
tk.Button(root, text="Sottrazione", command=sottrazione).pack(pady=10)
tk.Button(root, text="Moltiplicazione", command=moltiplicazione).pack()
tk.Button(root, text="Divisione", command=divisione).pack()

root.mainloop()
