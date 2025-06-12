import tkinter as tk
from tkinter import messagebox

class MenuMessageboxApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu con messagebox")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Info", command=self.mostra_info)
        self.root.geometry("350x150")
    def mostra_info(self):
        messagebox.showinfo("Informazione", "Questo è un messagebox di info.")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuMessageboxApp()
    app.run()
