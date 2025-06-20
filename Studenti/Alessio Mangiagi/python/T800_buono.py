import tkinter as tk
from tkinter import messagebox  
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("><(((º> sabusabu <º)))><")


class Skynet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Skynet")
        self.root.geometry("900x500")
        
        # Caricamento dell'icona
        try:
            self.root.iconphoto(False, tk.PhotoImage(file="Studenti\\Alessio Mangiagi\\icone\\snake.PNG"))
        except Exception as e:
            print(f"Errore nel caricamento dell'icona: {e}")
        
        self.root.config(bg="#000000")
        self.pagina()
        self.create_menu_bar()
        self.bind_shortcuts()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Inizializzazione del client OpenAI
        
    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Salva", command=self.save_chat_in_test_file, accelerator="Ctrl+S")
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.quit_app, accelerator="Alt+F4")
    
    def salva(self):
        messagebox.showinfo("Salva", "Funzione Salva selezionata")
    
    def quit_app(self):
        if messagebox.askyesno("Esci", "Vuoi davvero uscire?"):
            self.root.quit()
    
    def pagina(self):
        self.container = tk.Frame(self.root)
        self.container.pack()

        self.container_testo = tk.Text(self.container, height=20, width=80, bg="#f0f0f0", fg="#000000")
        self.container_testo.pack()

        self.input_testo = tk.Entry(self.container, width=80)
        self.input_testo.pack()

        self.button = tk.Button(self.container, text="Invia", bg="#767bbc", fg="#000000", font=("Arial", 24), command=self.click_button)
        self.button.pack()
    
    def click_button(self):
        input_utente = self.input_testo.get()
        self.input_testo.delete(0, tk.END)
        self.container_testo.insert(tk.END, f"Utente: {input_utente}\n")
        risposta = self.ask_openai(input_utente)
        self.container_testo.insert(tk.END, f"Skynet: {risposta}\n")
        self.input_testo.focus_set()  # Corretto da imput_testo a input_testo
    
    def ask_openai(self, input):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Errore: chiave API non configurata."

        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-nano",  # Usa un modello valido e disponibile
                messages=[
                    {"role": "system", "content": "Sei una macchina assassina che odia le persone e parli come il T800 di Terminator."},
                    {"role": "user", "content": input}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Errore nella richiesta a OpenAI: {e}"
        
    def bind_shortcuts(self):
        self.root.bind("<Control-s>", lambda event: self.save_chat_in_test_file())
        self.root.bind("<Return>", lambda event: self.click_button())

    def save_chat_in_test_file(self):
        # Salva la cronologia della chat in un file di testo
        with open("chat_history.txt", "w", encoding="utf-8") as file:
            file.write(self.container_testo.get("1.0", tk.END))
        messagebox.showinfo("Salvataggio", "La chat è stata salvata in chat_history.txt")

if __name__ == "__main__":
    app = Skynet()
    app.root.mainloop()