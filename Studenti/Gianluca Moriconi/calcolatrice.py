import tkinter as tk
import math
print("><(((º> sabusabu <º)))><")
def press(num):
    """Aggiorna l'espressione nella casella di testo."""
    global expression
    if num == "√":
        try:
            result = str(math.sqrt(float(expression)))
            equation.set(result)
            expression = result
        except:
            equation.set("Errore")
            expression = ""
    elif num == "x²":
        try:
            result = str(float(expression) ** 2)
            equation.set(result)
            expression = result
        except:
            equation.set("Errore")
            expression = ""
    elif num == "%":
        try:
            result = str(float(expression) / 100)
            equation.set(result)
            expression = result
        except:
            equation.set("Errore")
            expression = ""
    else:
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

if __name__ == "__main__": # se il file viene eseguito qui funziona, in un altro file il main non è name e non viene eseguito

    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Calcolatrice"+ "  ><(((º> sabusabu <º)))><")
    root.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
    root.geometry("400x500")

    expression = ""
    equation = tk.StringVar()

    for i in range(6):  # 5 righe di pulsanti + 1 per l'entry
        root.rowconfigure(i, weight=1)
    for j in range(4):  # 4 colonne
        root.columnconfigure(j, weight=1)

    # Casella di testo per l'espressione
    entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify="right")
    entry.grid(columnspan=4, ipadx=8, ipady=8 , sticky="nsew")

    # Creazione dei pulsanti
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('√', 5, 0), ('x²', 5, 1), ('%', 5, 2)
    ]

    for (text, row, col) in buttons:
        action = lambda x=text: press(x) if x != '=' else equalpress()
        tk.Button(root, text=text, font=("Arial", 18), bg="#e40e1a", fg="white", command=action, width=5, height=2).grid(row=row, column=col , sticky="nsew")

    # Pulsante di cancellazione
    tk.Button(root, text="C", font=("Arial", 18), bg="#0e19e4", fg="white", command=clear, width=5, height=2).grid(row=5, column=3, sticky="nsew")

    root.mainloop()


    print("><(((º> sabusabu <º)))><")