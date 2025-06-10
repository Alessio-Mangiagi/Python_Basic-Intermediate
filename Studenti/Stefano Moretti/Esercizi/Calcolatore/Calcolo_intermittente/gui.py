import tkinter as tk
from utils import *
from intermittente import *

# Creiamo la finestra principale
root = tk.Tk()
root.title("Calcolatore Digiuno Intermittente")
root.geometry("600x600")
root.configure(bg="#2b2b2b")

# Creiamo etichette e campi
label_ore_digiuno = tk.Label(root, text="Quante ore vuoi digiunare? (Inserisci un numero da 0 a 24): ", font=("Helvetica", 14), bg="#2b2b2b", fg="#ffffff")
label_ore_digiuno.grid(row=0, column=0, padx=10, pady=25)

entry_ore_digiuno = tk.Entry(root, font=("Helvetica", 16))
entry_ore_digiuno.grid(row=1, column=0, padx=10, pady=25)

label_finito_mangiare = tk.Label(root, text="A che ora hai finito di mangiare?: ", font=("Helvetica", 14), bg="#2b2b2b", fg="#ffffff")
label_finito_mangiare.grid(row=2, column=0, padx=10, pady=25)
entry_finito_mangiare = tk.Entry(root, font=("Helvetica", 16))
entry_finito_mangiare.grid(row=3, column=0, padx=10, pady=25)





root.mainloop()


