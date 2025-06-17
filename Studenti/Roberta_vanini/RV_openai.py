from openai import OpenAI
import tkinter as tk

class mainframe:
    def __init__(self):
        self.root= tk.Tk()
        self.root.title("My Ai-chat interface")
        self.root.geometry("900X500")
        self.root.config(bg= "lightblue")
        self.pagina()

    def pagina(self):
        self.container = tk.Frame(self.root)
        self.container_testo = tk.Text(self.container)
        self.container.pack()
        self.container_testo.pack()
        self.input_testo = tk.Entry(self.container)
        self.input_testo.pack()
        self.button = tk.Button(self.container, text= "invia")
        self.button.pack()

        self.root.mainloop()


if __name__ == "__main__":
    app = mainframe()
    app.root.mainloop()