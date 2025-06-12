import tkinter as tk
from tkinter import messagebox

class MenuAskApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AskYesNo e AskQuestion")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Domande", menu=filemenu)
        filemenu.add_command(label="Chiedi Sì/No", command=self.chiedi_si_no)
        filemenu.add_command(label="Chiedi Domanda", command=self.chiedi_domanda)
        filemenu.add_command(label="Chiedi Ok/Annulla", command=self.chiedi_ok_annulla)
        self.root.geometry("350x150")
    def chiedi_si_no(self):
        risposta = messagebox.askyesno("Conferma", "Vuoi continuare?")
        print("Risposta Sì/No:", risposta)
    def chiedi_domanda(self):
        risposta = messagebox.askquestion("Domanda", "Sei sicuro?")
        print("Risposta Domanda:", risposta)
    def chiedi_ok_annulla(self):
        risposta = messagebox.askokcancel("Conferma", "Vuoi procedere?")
        print("Risposta Ok/Annulla:", risposta)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuAskApp()
    app.run()
