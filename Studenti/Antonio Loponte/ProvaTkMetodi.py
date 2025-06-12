import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mia prova")
        self.geometry("300x200")




        self.label = tk.Label(self, text="Ciao, mondo!")
        self.label.pack(pady=20)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=10)


        self.button = tk.Button(self, text="Cliccami", command=self.mostra_messaggio)   
        self.button.pack(pady=10)


    def mostra_messaggio(self):
        nome = self.entry_nome.get()
        self.label_saluto=tk.Label(self, text=f"Ciao, {nome}!")
        self.label_saluto.pack(pady=10)




prova = App()
prova.mainloop()