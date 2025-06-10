import tkinter as tk

# Crea la finestra principale
root = tk.Tk()
root.title("Esempio RadioButton")

# Variabile per memorizzare la scelta
scelta = tk.StringVar(value="Opzione 1")

# Funzione per mostrare la scelta selezionata
def mostra_scelta():
    label_risultato.config(text=f"Hai scelto: {scelta.get()}")

# Crea i radiobutton
radio1 = tk.Radiobutton(root, text="Opzione 1", variable=scelta, value="Opzione 1", command=mostra_scelta)
radio2 = tk.Radiobutton(root, text="Opzione 2", variable=scelta, value="Opzione 2", command=mostra_scelta)
radio3 = tk.Radiobutton(root, text="Opzione 3", variable=scelta, value="Opzione 3", command=mostra_scelta)

radio1.pack(anchor='w')
radio2.pack(anchor='w')
radio3.pack(anchor='w')

# Etichetta per mostrare la scelta
label_risultato = tk.Label(root, text="Hai scelto: Opzione 1")
label_risultato.pack(pady=10)

# Avvia il ciclo principale di tkinter
root.mainloop()
