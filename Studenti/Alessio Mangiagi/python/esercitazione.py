import tkinter as tk

class App(tk.Tk):  # Rinominata la classe in PascalCase
    def __init__(self):
        super().__init__()
        self.title("Esercitazione")
        self.geometry("600x600")
        self.iconbitmap("Studenti/Alessio Mangiagi/icone/favicon.ico")
        self.configure(bg="#3653D1")
        
       
        self.label_nome = tk.Label(self, text="Inserisci il tuo nome:",bg="#3653D1", fg="white", font=("Arial", 24))
        self.label_nome.pack(pady=20)
        
        self.entry_nome = tk.Entry(self, bg="#ffffff",fg="#000000", font=("Arial", 24))
        self.entry_nome.pack(pady=20)
        
        self.label_saluto = tk.Label(self, text="Ciao", bg="#3653D1", fg="white",font=("Arial", 24))
        self.label_saluto.pack(pady=20)
        
        # Correzione del binding dell'evento
        self.entry_nome.bind("<Return>", self.saluto)
        
    def create_widgets(self):
        self.label = tk.Label(self, text="Esercitazione", bg="#3653D1", fg="white",font=("Arial", 24))
        self.label.pack(pady=20)
     
    def saluto(self, event):
        nome = self.entry_nome.get()
        self.label_saluto.config(text=f"Ciao {nome}")
        
if __name__ == "__main__":    
    app = App()  # Usa il nome corretto della classe
    app.mainloop()