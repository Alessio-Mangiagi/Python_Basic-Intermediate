import tkinter as tk

class MenuAzioniApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu con azioni")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Saluta", command=self.saluta)
        filemenu.add_command(label="Esci", command=self.root.quit)
        self.root.geometry("350x150")
        self.label = tk.Label(self.root, text="Clicca su Saluta nel menu File")
        self.label.pack(pady=40)
    def saluta(self):
        self.label.config(text="Ciao dal menu!")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuAzioniApp()
    app.run()
