import tkinter as tk

# Creazione della finestra principale
window = tk.Tk()
window.title("Interfaccia utente")
window.geometry("400x300")

# Creazione di un'etichetta
label = tk.Label(window, text="Inserisci i tuoi dati", font=("Segoe", 14, "bold"))
label.pack()

camp_testo1 = tk.Entry(window)
camp_testo1.pack()

# Creazione di una funzione pulsante
def azione_pulsante():
    print("Accesso eseguito!")

pulsante1 = tk.Button(window, text="Accedi", command=azione_pulsante)
pulsante1.pack()

window.mainloop()