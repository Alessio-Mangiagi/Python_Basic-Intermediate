import tkinter as tk
from tkinter import messagebox

class MenuMessageTypesApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tipi di messagebox")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Messaggi", menu=filemenu)
        filemenu.add_command(label="Info", command=self.info)
        filemenu.add_command(label="Warning", command=self.warning)
        filemenu.add_command(label="Errore", command=self.errore)
        self.root.geometry("350x150")
    def info(self):
        messagebox.showinfo("Info", "Messaggio informativo.")
    def warning(self):
        messagebox.showwarning("Attenzione", "Messaggio di warning!")
    def errore(self):
        messagebox.showerror("Errore", "Messaggio di errore!")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuMessageTypesApp()
    app.run()
