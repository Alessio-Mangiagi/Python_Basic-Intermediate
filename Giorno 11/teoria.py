import tkinter


import tkinter as tk


def press(num):
    """Aggiorna l'espressione nella casella di testo."""
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    """Valuta l'espressione e mostra il risultato."""
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Errore")
        expression = ""


def clear():
    """Cancella il contenuto della casella di testo."""
    global expression
    expression = ""
    equation.set("")
    listbox.delete(0, tk.END)  # Pulisce la Listbox quando si cancella l'espressione


# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice")
root.geometry("300x600")

expression = ""
equation = tk.StringVar()

# Casella di testo per l'espressione
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify="right")
entry.grid(columnspan=4, ipadx=8, ipady=8)

# Creazione dei pulsanti
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("=", 4, 3),
]

for text, row, col in buttons:
    action = lambda x=text: press(x) if x != "=" else equalpress()
    tk.Button(
        root, text=text, font=("Arial", 18), command=action, width=5, height=2
    ).grid(row=row, column=col)

# Pulsante di cancellazione
tk.Button(root, text="C", font=("Arial", 18), command=clear, width=5, height=2).grid(
    row=5, column=0, columnspan=4
)

listbox = tk.Listbox(
    root,
    selectmode=tk.EXTENDED,
    bg="white",
    fg="black",
    selectbackground="blue",
    selectforeground="white",
    justify=tk.CENTER,
)
listbox.insert(tk.END, "Ciao")
listbox.insert(tk.END, "Mondo")
listbox.insert(tk.END, "Python")
listbox.insert(tk.END, "Tkinter")


def on_select(event):
    indici = listbox.curselection()  # Ottiene l'indice dell'elemento selezionato
    elementi = [listbox.get(i) for i in indici]  # Ottiene gli elementi selezionati
    print("Elementi selezionati:", elementi)


listbox.bind("<<ListboxSelect>>", on_select)  # Associa l'evento di selezione
listbox.grid(row=6, column=0, columnspan=4, sticky="nsew")


root.mainloop()

# rendere la finetstra piu elastica
