import tkinter as tk

def on_select(event):
    print("")

def add_item():
    new_item = entry.get().strip()
    if new_item:  # verifica se l'input non è vuoto
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)  # pulisce l'input dopo l'aggiunta


root = tk.Tk()
root.title("Lista della spesa")
root.geometry("600x400")

listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 14), height=10, width=25)
listbox.pack(side=tk.LEFT, fill=tk.Y)

listbox.bind("<<ListboxSelect>>", on_select) # associa l'evento di selezione

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
left_frame.pack_propagate(False)

# Spaziatore sopra
tk.Frame(left_frame).pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(left_frame, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=10)

add_button = tk.Button(left_frame, text="Aggiungi", font=("Arial", 14), command=add_item)
add_button.pack(fill=tk.X, padx=10, pady=10)

delete_button = tk.Button(left_frame, text="Elimina", font=("Arial", 14), command=lambda: listbox.delete(tk.ANCHOR))
delete_button.pack(fill=tk.X, padx=10, pady=10)

# Spaziatore sotto
tk.Frame(left_frame).pack(fill=tk.BOTH, expand=True)

# avvia loop alla fine del codice
root.mainloop()