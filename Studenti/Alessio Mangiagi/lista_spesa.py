import tkinter as tk
from tkinter import messagebox

print("><(((º> sabusabu <º)))><")

# Lista della spesa
class ListaSpesa:
    def __init__(self, root):
        self.root = root
        root.title("Lista della Spesa")
        root.geometry("900x400")
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
        
        #check box
        self.check_var = tk.BooleanVar()
        self.check_button = tk.Checkbutton(main, text="Mostra somma", variable=self.check_var, bg="#3653D1", fg="white", font=("Arial", 14))
        self.check_button.pack(pady=10)

        self.items = []
        self.prices = []  # Nuova lista per i prezzi

        self.label = tk.Label(barra, text="Inserisci un elemento:", bg="#f0f0f0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(barra)
        self.entry.pack(pady=5, padx=10, fill=tk.X)
        self.entry.focus()

        # Nuova entry per il prezzo
        self.price_label = tk.Label(barra, text="Prezzo:", bg="#f0f0f0")
        self.price_label.pack(pady=2)
        self.price_entry = tk.Entry(barra)
        self.price_entry.pack(pady=5, padx=10, fill=tk.X)

        self.add_button = tk.Button(barra, text="Aggiungi", command=self.add_item)
        self.add_button.pack(pady=5)

        # Modifica la listbox per mostrare nome e prezzo
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.remove_button = tk.Button(barra, text="Rimuovi selezionato", command=self.remove_item)
        self.remove_button.pack(pady=5)

        # Bottone per salvare su TXT
        self.save_txt_button = tk.Button(barra, text="Salva su TXT", command=self.salva_su_txt)
        self.save_txt_button.pack(pady=10)

    def add_item(self):
        item = self.entry.get()
        price = self.price_entry.get()
        if item and price:
            try:
                prezzo_float = float(price)
            except ValueError:
                messagebox.showwarning("Attenzione", "Inserisci un prezzo valido (numero).")
                return
            self.items.append(item)
            self.prices.append(prezzo_float)
            # Mostra sia nome che prezzo nella listbox
            self.listbox.insert(tk.END, f"{item} - €{prezzo_float:.2f}")
            self.entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Attenzione", "Inserisci sia un elemento che un prezzo.")

    def remove_item(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.items[selected_index]
            del self.prices[selected_index]
            self.listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Attenzione", "Seleziona un elemento da rimuovere.")
            
    def salva_su_txt(self):
        if not self.items:
            messagebox.showinfo("Info", "La lista è vuota, niente da salvare.")
            return
        try:
            with open("lista_spesa.txt", "w", encoding="utf-8") as f:
                f.write("Prodotto\tPrezzo (€)\n")
                f.write("-" * 25 + "\n")
                for item, prezzo in zip(self.items, self.prices):
                    f.write(f"{item}\t€{prezzo:.2f}\n")
                f.write("-" * 25 + "\n")
                totale = sum(self.prices)
                f.write(f"Totale:\t€{totale:.2f}\n")
            messagebox.showinfo("Salvato", "Lista salvata in lista_spesa.txt")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il salvataggio: {e}")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaSpesa(root)
    root.mainloop()
    
    
    
'''aggiungere  una variabile booleana globale per attivare o disattivare la visualizzazione della somma degli elementi
    e un metodo per calcolare la somma degli elementi della lista quando la casella di controllo è selezionata. 
    oltre ad una def che riesca se flaggata di attivare il delete per rimuovere gli elementi selezionati dalla lista.'''
#a paint aggiungere una casella di testo con # esadecimale per il colore di sfondo della finestra principale
# e un metodo per cambiare il colore di sfondo della finestra principale in base al colore selezionato.