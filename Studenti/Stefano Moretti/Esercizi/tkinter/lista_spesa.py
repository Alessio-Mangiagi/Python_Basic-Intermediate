import tkinter as tk

def on_select(event):
    print("")

def add_item():
    new_item = entry.get().strip()
    
    if new_item:
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)

def delete_selected():
    selected_index = listbox.curselection()
    
    for i in selected_index:
        listbox.delete(i)           

root = tk.Tk()
root.title("Lista della Spesa")
root.geometry("700x400")



listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 14), width=20)
listbox.pack(side=tk.LEFT, fill=tk.Y)
listbox.bind("<<ListboxSelect>>", on_select)  # Associa l'evento di selezione alla funzione

entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack(side=tk.LEFT)

add_button = tk.Button(root, text="Aggiungi", font=("Arial", 14), command=lambda: add_item())
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(root, text="Elimina Selezione", font=("Arial", 14), command=lambda: delete_selected())
delete_button.pack(side=tk.LEFT)

text_area = tk.Text(root, font=("Arial", 14), width=40, height=10)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()