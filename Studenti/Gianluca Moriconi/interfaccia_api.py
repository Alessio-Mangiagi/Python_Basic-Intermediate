import tkinter as tk
from tkinter import messagebox
import openai as OpenAI
from dotenv import load_dotenv
import os

class skynet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Skynet")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#404040")
        self.pagina()

    def pagina(self):
        self.container = tk.Frame(self.root, bg="#404040")
        self.container_testo = tk.Text(self.container)
        self.container.pack()
        self.container_testo.pack()
        self.input_testo = tk.Entry(self.container)
        self.input_testo.pack()
        self.button = tk.Button(self.container, text="Invia", command=self.on_button_click)
        self.button.pack(side="left")

    def on_button_click(self):
        testo = self.input_testo.get()
        self.container_testo.delete(0, tk.END)

       
    def ask_openai(self, input):
        client = OpenAI.OpenAI(api_key="YOUR_OPENAI_API_KEY")
        completion = client.chat.completions.create(model="gpt-4o-mini",store=True,messages=[{"role": "user", "content": input}])


        print(completion.choices[0].message)
    
if __name__ == "__main__":
        app = skynet()
        app.root.mainloop()
        