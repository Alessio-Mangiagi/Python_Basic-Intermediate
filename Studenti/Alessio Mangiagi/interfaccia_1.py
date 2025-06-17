import tkinter as tk
from tkinter import messagebox  
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  


print("><(((º> sabusabu <º)))><")


class skynet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("skynet")
        self.root.geometry("900x500")
        self.rooticonbitmap = tk.PhotoImage(file="Studenti\\Alessio Mangiagi\\icone\\snake.PNG")
        self.root.config(bg="#000000")
        self.pagina()
        
    def pagina(self):
        self.container = tk.Frame(self.root)
        self.continar_testo = tk.Text(self.container)
        self.container.pack()
        self.continar_testo.pack()
        self.imput_testo = tk.Entry(self.container)
        self.imput_testo.pack()
        self.button = tk.Button(self.container, text="invia", bg="#767bbc", fg="#000000", font=("Arial", 24), command=self.click_Button)
        self.button.pack()
    
    
    def click_Button(self):
        self.imput_utente = self.imput_testo.get()
        self.imput_testo.delete(0, tk.END)
        self.continar_testo.insert(tk.END, self.ask_openai(self.imput_utente))
    
    
    def ask_openai(self,input):
        client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
            )

        completion = client.chat.completions.create(model="gpt-4.1-nano",store=True,messages=[{"role": "user", "content": input}])

        return  completion.choices[0].message.content.strip()

    
if __name__ == "__main__":
    app = skynet()
    app.root.mainloop()
