import tkinter as tk
import math
from tris import Tris  # Importa la classe Tris dal file tris.py

### applicazione con menu su sx con più funzioni (giochi, tools e settings)
### parte destra l'applicativo

# Funzioni per mostrare i frame specifici
# Queste funzioni verranno chiamate dai bottoni del menu

def show_calcolatrice():
    calcolatrice_frame.pack(fill="both", expand=True)
    tris_frame.pack_forget()  # nascondi il frame dei tris

def show_tris():
    tris_frame.pack(fill="both", expand=True)
    calcolatrice_frame.pack_forget()  # nascondi il frame della calcolatrice

def show_tools():
    # Qui puoi aggiungere il codice per mostrare il frame dei tools
    pass

def show_settings():
    # Qui puoi aggiungere il codice per mostrare il frame delle impostazioni
    pass

# Funzioni per la calcolatrice

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

# creazione finestra
root = tk.Tk()
root.title("La mia applicazione")   #diamogli un titolo
root.geometry("1200x720")            #stabiliamo le dimensioni
root.configure(bg="#3C3535")

# creazione dei frame
menu = tk.Frame(root, bg="#000000", width=300, height=720)
menu.pack(side="left", fill="y")

bottom_menu = tk.Frame(menu, bg="#000000", width=300, height=150)
bottom_menu.pack(side="bottom", fill="x")

# crazione frame principale
main_frame = tk.Frame(root, bg="#3C3535", width=900, height=720)
main_frame.pack(side="right", fill="both", expand=True)

label_benvenuto = tk.Label(main_frame, text="Benvenuto nella mia applicazione!", bg="#3C3535", fg="#FFFFFF", font=("Arial", 24))
label_scegli = tk.Label(main_frame, text="Scegli un'opzione dal menu a sinistra.", bg="#3C3535", fg="#FFFFFF", font=("Arial", 16))
label_clicca = tk.Label(main_frame, text="Clicca su calcolatrice, tris, etc per aprire l'applicazione desiderata", bg="#3C3535", fg="#FFFFFF", font=("Arial", 16))

label_benvenuto.place(relx=0.5, rely=0.1, anchor="n")
label_scegli.place(relx=0.5, rely=0.4, anchor="n")
label_clicca.place(relx=0.5, rely=0.5, anchor="n")

calcolatrice_frame = tk.Frame(main_frame, bg="#3E4C68", width=900, height=720)

## creazione calcolatrice
expression = ""
equation = tk.StringVar()

for i in range(6):  # 5 righe di pulsanti + 1 per l'entry
    calcolatrice_frame.rowconfigure(i, weight=1)
for j in range(4):  # 4 colonne
    calcolatrice_frame.columnconfigure(j, weight=1)

# Casella di testo per l'espressione
entry = tk.Entry(calcolatrice_frame, textvariable=equation, font=("Arial", 20), justify="right")
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
    tk.Button(calcolatrice_frame, text=text, font=("Arial", 18), bg="#e40e1a", fg="white", command=action, width=5, height=2).grid(row=row, column=col , sticky="nsew")

# Pulsante di cancellazione
tk.Button(calcolatrice_frame, text="C", font=("Arial", 18), bg="#0e19e4", fg="white", command=clear, width=5, height=2).grid(row=5, column=3, sticky="nsew")

tris_frame = tk.Frame(main_frame, bg="#683E68", width=900, height=720)
tris_game = Tris(tris_frame)  # Crea il gioco del Tris passando il frame

# crazione bottoni 
calcolatrice_button = tk.Button(menu, text="Calcolatrice", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
calcolatrice_button.config(command=show_calcolatrice)  # associa il bottone alla funzione
calcolatrice_button.pack(pady=10)

tris_button = tk.Button(menu, text="Tris", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
tris_button.config(command=show_tris)  # associa il bottone alla funzione
tris_button.pack(pady=10)

tools_button = tk.Button(menu, text="Tools", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
tools_button.pack(pady=10)

settings_button = tk.Button(bottom_menu, text="Settings", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
settings_button.pack(pady=10)

root.mainloop() # per avvio, da mettere alla fine del codice