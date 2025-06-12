import tkinter as tk

class MenuIntroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Intro")
        # Creazione di una menubar vuota
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        self.root.geometry("300x150")
        label = tk.Label(self.root, text="Menu vuoto (intro)")
        label.pack(pady=40)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuIntroApp()
    app.run()
