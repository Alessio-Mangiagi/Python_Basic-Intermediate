import tkinter as tk

class MenuTendinaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu a tendina e sottomenu")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        # Sottomenu
        submenu = tk.Menu(filemenu, tearoff=0)
        submenu.add_command(label="Opzione 1")
        submenu.add_command(label="Opzione 2")
        filemenu.add_cascade(label="Sottomenu", menu=submenu)
        # Sotto-Sottomenu
        subsubmenu = tk.Menu(submenu, tearoff=0)
        subsubmenu.add_command(label="Sotto-opzione 1")
        subsubmenu.add_command(label="Sotto-opzione 2")
        submenu.add_cascade(label="Sottomenu", menu=subsubmenu)
        self.root.geometry("350x150")
        label = tk.Label(self.root, text="Menu con sottomenu")
        label.pack(pady=40)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuTendinaApp()
    app.run()
