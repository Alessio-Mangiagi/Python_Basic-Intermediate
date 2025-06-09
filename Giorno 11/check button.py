import tkinter as tk

# Crea la finestra principale
root = tk.Tk()
root.title("Esempio Checkbutton")

# Variabile associata al Checkbutton
var = tk.BooleanVar()

# Funzione chiamata quando il Checkbutton viene selezionato/deselezionato
def on_check():
    if var.get():
        print("Checkbutton selezionato")
    else:
        print("Checkbutton deselezionato")

# Crea il Checkbutton
check = tk.Checkbutton(root, text="Seleziona", variable=var, command=on_check)
check.pack(padx=20, pady=20)

# Avvia il loop principale di Tkinter
root.mainloop()
