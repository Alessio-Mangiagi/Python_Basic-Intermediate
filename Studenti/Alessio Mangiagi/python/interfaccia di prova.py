import tkinter as tk
from tkinter import messagebox 
from openai import OpenAI 
import os
from dotenv import load_dotenv  
load_dotenv()
print("><(((º> sabusabu <º)))><")

class nuovo_chat:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChatboX")   
        self.root.geometry("900x500")    
        self.root.iconbitmap("Studenti\\Alessio Mangiagi\\icone\\favicon.ico")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = [{"role": "system", "content": "Sei un assistente gentile."}]
        self.create_menu_bar()
        self.create_widgets()
        self.bind_shortcuts()

    def create_menu_bar(self):
        """Crea la barra del menu"""
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Apri", command=self.apri, accelerator="Ctrl+O")
        filemenu.add_command(label="Salva", command=self.salva_text_area, accelerator="Ctrl+S")  
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.quit_app)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def create_widgets(self):
        """Crea i widget dell'interfaccia"""
        self.label = tk.Label(
            self.root, 
            text="Scrivi un messaggio e premi Invio o il pulsante Invia",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
        self.entry.bind("<Return>", lambda e: self.invia_messaggio())

        self.text_area = tk.Text(self.root, height=15, font=("Arial", 12))
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.invia_button = tk.Button(self.root, text="Invia", command=self.invia_messaggio, bg="#4750d2", fg="white")
        self.invia_button.pack(pady=5)

        self.create_toolbar()

    def bind_shortcuts(self):
        """Associa gli shortcut ai comandi"""
        self.root.bind("<Control-o>", lambda e: self.apri())
        self.root.bind("<Control-s>", lambda e: self.salva_text_area())
        # L'entry è già collegata a <Return> in create_widgets, non serve duplicare qui

    def invia_messaggio(self):
        """Invia il messaggio a OpenAI e mostra la risposta"""
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.text_area.insert(tk.END, f"Utente: {user_input}\n")
        self.messages.append({"role": "user", "content": user_input})
        self.entry.delete(0, tk.END)
        self.root.update_idletasks()
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-nano",  # Usa un modello valido e disponibile
                messages=self.messages,
                max_tokens=150
            )
            reply = response.choices[0].message.content
            self.text_area.insert(tk.END, f"Assistant: {reply}\n")
            self.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            self.text_area.insert(tk.END, f"Errore API: {e}\n")

    def apri(self):
        """Gestisce il comando Apri"""
        self.label.config(text="Hai cliccato Apri")
        messagebox.showinfo("Apri", "Funzione Apri selezionata")

    def salva_text_area(self):
        """Salva il contenuto della text_area in un file di testo"""
        contenuto = self.text_area.get("1.0", tk.END).strip()
        if contenuto:
            try:
                with open("contenuto_chat.txt", "w", encoding="utf-8") as f:
                    f.write(contenuto)
                messagebox.showinfo("Salva", "Contenuto salvato in contenuto_chat.txt")
            except Exception as e:
                messagebox.showerror("Errore", f"Errore nel salvataggio: {e}")
        else:
            messagebox.showwarning("Attenzione", "La finestra di testo è vuota.")

    def quit_app(self):
        """Chiude l'applicazione con conferma"""
        if messagebox.askyesno("Esci", "Vuoi davvero uscire?"):
            self.root.quit()

    def show_info(self):
        """Mostra informazioni nella console"""
        print("Mostra informazioni")

    def show_message(self):
        """Mostra un messaggio nella finestra di dialogo"""
        message = self.entry.get()
        if message:
            messagebox.showinfo("Messaggio", message)
        else:
            messagebox.showwarning("Attenzione", "Inserisci un messaggio da visualizzare.")

    def create_toolbar(self):
        """Crea una toolbar con pulsanti"""
        toolbar = tk.Frame(self.root, bg="#292A33", bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        bottone_clear = tk.Button(toolbar, text="Pulisci", command=self.clear_entry, bg="#4750d2", fg="white")
        bottone_clear.pack(side=tk.LEFT, padx=2, pady=2)

        bottone_info = tk.Button(toolbar, text="Mostra Messaggio", command=self.show_message, bg="#4750d2", fg="white")
        bottone_info.pack(side=tk.LEFT, padx=2, pady=2)

    def clear_entry(self):
        """Pulisce il contenuto dell'entry"""
        self.entry.delete(0, tk.END)
        

if __name__ == "__main__":
    app = nuovo_chat()
    app.root.mainloop()
    print("><(((º> sabusabu <º)))><")