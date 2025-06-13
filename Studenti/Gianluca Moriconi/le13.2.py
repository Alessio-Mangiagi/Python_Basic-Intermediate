import tkiner as tk
from tkinter import messagebox

class MenuBaseApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Base")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        # Aggiunta di un menu File
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.geometry("300x150")
        label = tk.Label(self.root, text="Menu base con File")
        label.pack(pady=40)

    def run(self):
        self.root.mainloop

if __name__ == "__main__":
    app = MenuBaseApp()
    app.run()