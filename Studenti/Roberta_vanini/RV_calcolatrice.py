import tkinter as tk

def get_values():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        return x, y
    except ValueError:
        result_label.config(text="Inserisci solo numeri!", fg="#F63131")
        return None, None

def addizione():
    x, y = get_values()
    if x is not None and y is not None:
        risultato = x + y
        result_label.config(text=f"Il risultato di {x} + {y} è {risultato}", fg="#FFC400")

def sottrazione():
    x, y = get_values()
    if x is not None and y is not None:
        risultato = x - y
        result_label.config(text=f"Il risultato di {x} - {y} è {risultato}", fg="#FFC400")

def moltiplicazione():
    x, y = get_values()
    if x is not None and y is not None:
        risultato = x * y
        result_label.config(text=f"Il risultato di {x} x {y} è {risultato}", fg="#FFC400")

def divisione():
    x, y = get_values()
    if x is not None and y is not None:
        try:
            risultato = x / y
            result_label.config(text=f"Il risultato di {x} / {y} è {risultato}", fg="#FFC400")
        except ZeroDivisionError:
            result_label.config(text="Errore: Non si può dividere per 0", fg="#F63131")

# creazione finestra

root = tk.Tk()
root.title("Calcolatrice")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#404040")

# creazione di un frame al centro
center_frame = tk.Frame(root, bg="#404040")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Frame per input numeri
input_frame = tk.Frame(center_frame, bg="#404040")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Primo numero:", bg="#404040", fg="#FFC400", font=("Arial", 14)).pack(pady=5)
entry_x = tk.Entry(input_frame, font=("Arial", 14))
entry_x.pack(pady=5)

tk.Label(input_frame, text="Secondo numero:", bg="#404040", fg="#FFC400", font=("Arial", 14)).pack(pady=5)
entry_y = tk.Entry(input_frame, font=("Arial", 14))
entry_y.pack(pady=5)

# Sposta la creazione di result_label qui sotto i pulsanti

# Primo frame per + e -
row1 = tk.Frame(center_frame, bg="#404040")
row1.pack(pady=10)
button_più = tk.Button(row1, text="+", bg="#FFC400", command=addizione, font=("Arial", 40, "bold"), width=2)
button_più.pack(side="left", padx=10)
button_meno = tk.Button(row1, text="-", bg="#FFC400", command=sottrazione, font=("Arial", 40, "bold"), width=2)
button_meno.pack(side="left", padx=10)

# Secondo frame per x e /
row2 = tk.Frame(center_frame, bg="#404040")
row2.pack(pady=10)
button_per = tk.Button(row2, text="x", bg="#FFC400", command=moltiplicazione, font=("Arial", 40, "bold"), width=2)
button_per.pack(side="left", padx=10)
button_div = tk.Button(row2, text="/", bg="#FFC400", command=divisione, font=("Arial", 40, "bold"), width=2)
button_div.pack(side="left", padx=10)

# Label per il risultato (ora sotto i pulsanti)
result_label = tk.Label(center_frame, text="", bg="#404040", fg="#FFC400", font=("Arial", 18, "bold"))
result_label.pack(pady=20)

root.mainloop() #avvio schermata (A FINE CODICE)