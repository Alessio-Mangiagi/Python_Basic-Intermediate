import tkinter as tk

class MenuAddCommandApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu add_command")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Apri", command=self.apri)
        filemenu.add_command(label="Salva", command=self.salva)
        self.root.geometry("350x150")
        self.label = tk.Label(self.root, text="Clicca su Apri o Salva nel menu File")
        self.label.pack(pady=40)
    def apri(self):
        self.label.config(text="Hai cliccato Apri")
    def salva(self):
        self.label.config(text="Hai cliccato Salva")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuAddCommandApp()
    app.run()
