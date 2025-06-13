import tkinter as tk
from tkinter import messagebox

class SimpleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple App")
        self.root.geometry("400x500")
        self.root.iconbitmap("Studenti/Alessio Mangiagi/icone/favicon.ico")
        self.root.configure(bg="#3D6882")
    
    def clear(self):
        """Pulisce il contenuto della finestra."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp()
    root.mainloop()
    
     