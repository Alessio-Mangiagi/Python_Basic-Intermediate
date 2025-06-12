import tkinter as tk

class MenuSeparatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu con separatore")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Nuovo")
        filemenu.add_command(label="Apri")
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.quit)
        self.root.geometry("350x150")
        label = tk.Label(self.root, text="Menu con separatore tra Apri ed Esci")
        label.pack(pady=40)
    def run(self):
        self.root.mainloop()



    def quit(self):
        self.root.quit()

if __name__ == "__main__":
    app = MenuSeparatorApp()
    app.run()
