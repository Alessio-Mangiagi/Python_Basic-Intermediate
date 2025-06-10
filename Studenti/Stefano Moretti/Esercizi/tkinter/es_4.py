import tkinter as tk

def on_select(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_language = listbox.get(selected_indices[0])
        print(f"Hai selezionato: {selected_language}")

def add_item():
    new_item = entry.get()
    if new_item:
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Esempio di Listbox e Text")
root.geometry("600x400")

listbox = tk.Listbox(root, font=("Arial", 14), width=20)
listbox.pack(side=tk.LEFT, fill=tk.Y)
listbox.bind("<<ListboxSelect>>", on_select)

for elemento in [
    
]:
    listbox.insert(tk.END, elemento)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

btn = tk.Button(root, text="Aggiungi", font=("Arial", 14), command=add_item)
btn.pack(side=tk.TOP, pady=5)

btn_delete = tk.Button(
    root,
    text="Elimina Selezione",
    font=("Arial", 14),
    command=lambda: listbox.delete(tk.ANCHOR),
)
btn_delete.pack(side=tk.TOP, padx=10, pady=5)

text_area = tk.Text(root, font=("Arial", 14), height=10)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()


