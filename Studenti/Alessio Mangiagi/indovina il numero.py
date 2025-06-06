#indovina il numero
import random
import tkinter as tk

# Indovina il Numero 

class IndovinaNumeroGUI:
    def __init__(self, master):
        self.master = master
        master.title("Indovina il Numero!")
        self.reset_game()

        self.label = tk.Label(master, text="INDOVINA IL NUMERO!!!\nInserisci un numero tra 1 e 99")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Invia", command=self.check_number)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(master, text="Ricomincia", command=self.reset_game)
        self.restart_button.pack()

    def reset_game(self):
        self.x = random.randint(1, 99)
        self.tentativi = 0
        if hasattr(self, 'result_label'):
            self.result_label.config(text="")
        if hasattr(self, 'entry'):
            self.entry.delete(0, tk.END)

    def check_number(self):
        try:
            numero = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Inserisci un numero valido!")
            return
        self.tentativi += 1
        if self.x < numero:
            self.result_label.config(text="Troppo! RIPROVA")
        elif self.x > numero:
            self.result_label.config(text="Troppo poco! RIPROVA")
        else:
            self.result_label.config(text=f"{self.x} indovinato in {self.tentativi} tentativi!")

if __name__ == "__main__":
    root = tk.Tk()
    app = IndovinaNumeroGUI(root)
    root.mainloop()

