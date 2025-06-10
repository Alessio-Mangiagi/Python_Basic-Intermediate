import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()


def add_item():
    new_item = entry.get().strip()
    if new_item:
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Lista canzoni preferite")
root.geometry("1200x650")

listbox = tk.Listbox(root, selectmode=tk.EXTENDED, font=("Arial", 10), width=20)
listbox.pack(side=tk.LEFT, fill=tk.Y)
listbox.bind("<<ListboxSelect>>", on_select)

for elemento in [
    "Alba Chiara",
    "Siamo soli",
    "Rewind",
    "L'amore l'amore",
    "Io no",
    "Come stai",
    "Come nelle favole",
]:
    listbox.insert(tk.END, elemento)


btn = tk.Button(root, text="Aggiungi", font=("Arial", 14), command=add_item)
btn.pack(side=tk.TOP, padx=10, pady=5)  

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(
    side=tk.TOP, fill=tk.X, padx=10, pady=10
)  

text_area = tk.Text(root, font=("Arial", 14), height=10)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)


root.mainloop()