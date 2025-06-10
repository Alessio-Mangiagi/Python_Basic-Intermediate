import tkinter as tk
from tkinter import messagebox

print("><(((º> sabusabu <º)))><")

# Lista della spesa
class ListaSpesa:
    def __init__(self, root):
        self.root = root
        root.title("Lista della Spesa")
        root.geometry("400x400")
        root.iconbitmap("Studenti/Alessio Mangiagi/icone/favicon.ico")
        root.configure(bg="#3D6882")
        
        # menu
        self.menu = tk.Menu(root, bg="#3D6882", fg="white", activebackground="#4750d2", activeforeground="grey")    
        self.file_menu = tk.Menu(self.menu, tearoff=0, bg="#3D6882", fg="white", activebackground="#4750d2", activeforeground="#ff0000")    
        self.file_menu.add_command(label="Apri", command=lambda: print("Apri"))    
        self.file_menu.add_command(label="Salva", command=lambda: print("Salva"))    
        self.file_menu.add_separator()    
        self.file_menu.add_command(label="Esci", command=root.quit)    
        self.menu.add_cascade(label="File", menu=self.file_menu)    
        root.config(menu=self.menu)
        
        # main layout
        barra = tk.Frame(root, bg="#292A33")
        barra.pack(side="left", fill="y")
        barra_bassa = tk.Frame(barra, bg="#292A33")
        barra_bassa.pack(side="bottom", fill="y")

        main = tk.Frame(root, bg="#3653D1")
        main.pack(side="right", fill="both", expand=True)
        tk.Label(main, text="somma elementi", bg="#3653D1", fg="white", font=("Arial", 24)).pack(pady=20)

        self.items = []

        self.label = tk.Label(barra, text="Inserisci un elemento:", bg="#f0f0f0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(barra)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(barra, text="Aggiungi", command=self.add_item)
        self.add_button.pack( pady=5)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.remove_button = tk.Button(barra, text="Rimuovi selezionato", command=self.remove_item)
        self.remove_button.pack(pady=5)

    def add_item(self):
        item = self.entry.get()
        if item:
            self.items.append(item)
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Attenzione", "Inserisci un elemento da aggiungere.")

    def remove_item(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.items[selected_index]
            self.listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Attenzione", "Seleziona un elemento da rimuovere.")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaSpesa(root)
    root.mainloop()