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

root = tk.Tk()
root.title("Esempio Listbox Tkinter")

listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

# Aggiungi elementi alla Listbox
for elemento in ["Mela", "Banana", "Arancia", "Pera", "Uva"]:
    listbox.insert(tk.END, elemento)

btn = tk.Button(root, text="Mostra selezione", command=mostra_selezione)
btn.pack(pady=5)

root.mainloop()