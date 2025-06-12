import tkinter as tk

#L’esercizio prevede una mini-app che permette di inserire il proprio nome, cliccare un bottone oppure premere Invio per mostrare un saluto,
# e passare il mouse sopra la label per cambiarne il colore.

class App(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.title("Esercitazione 12")
        self.geometry("800x600")
        
        self.label_nome = tk.Label(self, text="Inserisci il tuo nome:")
        self.label_nome.pack(pady=10)
        
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=10)
        
        self.button_saluto = tk.Button(self, text="Saluto", command=self.mostra_saluto)
        self.button_saluto.pack(pady=10)
        self.entry_nome.bind("<Return>", lambda e: self.mostra_saluto())
    
    
    def mostra_saluto(self):
        nome = self.entry_nome.get()
        self.label_saluto = tk.Label(self, text=f"Ciao {nome}!")
        self.label_saluto.pack(pady=10)
        self.label_saluto.bind("<Enter>", lambda e: self.cambia_colore(e, "red"))
        self.label_saluto.bind("<Leave>", self.cambia_colore)
        
    def cambia_colore(self, event, colore="black"):
        self.label_saluto.config(fg=colore)
        
        
istanza_app = App()
istanza_app.mainloop()