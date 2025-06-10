import tkinter as tk
from tkinter import messagebox


# Funzione per mostrare l'elemento selezionato
def mostra_selezione():
    selezione = listbox.curselection()
    if selezione:
        valore = listbox.get(selezione[0])
        messagebox.showinfo("Selezione", f"Hai selezionato: {valore}")
    else:
        messagebox.showwarning("Attenzione", "Nessun elemento selezionato.")


def on_change():
    """Funzione per gestire il cambiamento dello stato del Checkbutton."""
    if var.get() == 1:
        listbox.select_set(0, tk.END)  # Seleziona tutti gli elementi

    else:
        listbox.select_clear(0, tk.END)  # Deseleziona tutti gli elementi


root = tk.Tk()
root.title("Esempio Listbox Tkinter")

listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

# Aggiungi elementi alla Listbox
for elemento in ["Mela", "Banana", "Arancia", "Pera", "Uva"]:
    listbox.insert(tk.END, elemento)

btn = tk.Button(root, text="Mostra selezione", command=mostra_selezione)
btn.pack(pady=5)
var = tk.IntVar()
check = tk.Checkbutton(root, text="Seleziona tutto", variable=var, command=on_change)
check.pack(pady=5)


root.mainloop()
