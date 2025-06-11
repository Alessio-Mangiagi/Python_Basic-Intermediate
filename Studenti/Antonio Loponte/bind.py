import tkinter as tk

def on_select(event):
    # Ottieni l'indice selezionato
    selection = listbox.curselection()
    if selection:
        value = listbox.get(selection[0])
        label_var.set(f"Hai selezionato: {value}")

root = tk.Tk()
root.title("Esempio di bind con Listbox")

listbox = tk.Listbox(root)
for item in ["Mela", "Banana", "Arancia", "Pera"]:
    listbox.insert(tk.END, item)
listbox.pack()

label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var)
label.pack()

listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
