"""

import tkinter as tk


def on_select(event):
    print("")

def add_item():
    #Aggiunge un nuovo elemento alla Listbox.
    # Ottiene il testo dalla casella di input e rimuove spazi vuoti
    new_item = entry.get().strip()

    # Controlla se il testo non è vuoto
    if new_item:
        # Aggiunge l'elemento alla fine della listbox
        listbox.insert(tk.END, new_item)
        # Pulisce la casella di testo dopo l'aggiunta
        entry.delete(0, tk.END)

def delete_item():
    #Elimina l'elemento selezionato dalla Listbox.
    # Ottiene gli indici degli elementi selezionati
    selected_index = listbox.curselection()
    for i in selected_index:
        listbox.delete(i)


root = tk.Tk()
root.title("title")
root.geometry("600x500")

# Creazione della Listbox con selezione multipla
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 14), width=20)
listbox.pack(side=tk.LEFT, fill=tk.Y)  # Posiziona a sinistra, riempie verticalmente
listbox.bind(
    "<<ListboxSelect>>", on_select
)  # Associa l'evento di selezione alla funzione

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(
    side=tk.LEFT
) 

add_button = tk.Button(root, text="Aggiungi", command=add_item, font=("Arial", 14))
add_button.pack(side=tk.LEFT)
delete_button = tk.Button(root, text="Rimuovi", command=delete_item, font=("Arial", 14))
delete_button.pack(side=tk.LEFT)

root.mainloop()
"""

#----------------------------------------------------------------------------------

