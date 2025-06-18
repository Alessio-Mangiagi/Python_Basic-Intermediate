from openai import OpenAI
from tkinter import messagebox
import tkinter as tk
import os



class mini_chatGpt:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini ChatGPT")
        self.root.geometry("800x600")
        icon_path = r"C:\Users\lopon\OneDrive\Desktop\Corso Python\Python_Basic-Intermediate\studenti\Antonio Loponte\icon.png"
        icon_img = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(True, icon_img)
        self.icon_img = icon_img  
        self.root.config(bg="#17d366")


    def pagina(self):
        self.container = tk.Frame(self.root)
        




if __name__ == "__main__":
    app = mini_chatGpt()
    app.root.mainloop()

# dotenv serve solo se vuoi caricare variabili d'ambiente da un file .env (ad esempio per la tua API key OpenAI).
# Se non usi variabili d'ambiente o non hai un file .env, non è necessario installarlo.
# Se vuoi usarlo, installa con:
# pip install python-dotenv

# Esempio di utilizzo:
# from dotenv import load_dotenv
# load_dotenv()
# import os
# api_key = os.getenv("OPENAI_API_KEY")