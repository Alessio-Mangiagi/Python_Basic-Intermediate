from openai import OpenAI
from tkinter import messagebox
import tkinter as tk
import os
from dotenv import load_dotenv


load_dotenv()  



class mini_chatGpt:
    def __init__(self):
        self.container = None  
        self.root = tk.Tk()
        self.container = tk.Frame(self.root)
        self.root.title("Mini ChatGPT")
        self.root.geometry("800x600")
        icon_path = r"C:\Users\lopon\OneDrive\Desktop\Corso Python\Python_Basic-Intermediate\studenti\Antonio Loponte\icon.png"
        icon_img = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(True, icon_img)
        self.icon_img = icon_img  
        self.root.config(bg="#17d366")
        menuchat = tk.Menu(self.root)
        self.root.config(menu=menuchat)
        file_menu = tk.Menu(menuchat, tearoff=0)
        menuchat.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Nuova Conversazione", command=self.pagina)
        file_menu.add_command(label="Esci", command=self.root.quit)
        self.chat_history = [
            {
                "role": "system",
                "content": "Al primo messaggio chiedi sempre all'utente di presentarsi e di dire qualcosa su di lui.",
            },
        ]

        
        self.chat_frame_container = tk.Frame(self.root, bg="#17d366")
        self.chat_frame_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20,0))

        self.canvas = tk.Canvas(self.chat_frame_container, bg="#17d366", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.chat_frame_container, orient="vertical", command=self.canvas.yview)
        self.chat_frame = tk.Frame(self.canvas, bg="#17d366")

        self.chat_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        bottom_frame = tk.Frame(self.root, bg="#17d366")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

        self.input_box = tk.Text(bottom_frame, height=5, width=60, font=("Arial", 14))
        self.input_box.pack(padx=(10,0), pady=10, side=tk.LEFT)

        self.genera_btn = tk.Button(
            bottom_frame, text="Genera", command=self.genera_risposta, bg="#0d0e0d", fg="white", font=("Arial", 14, "bold")
        )
        self.genera_btn.pack(padx=(10,20), pady=10, side=tk.LEFT)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def pagina(self):
    
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        self.input_box.delete("1.0", tk.END)

    def aggiungi_nuvoletta(self, testo, lato, colore_bg, colore_fg):
        nuvoletta = tk.Label(
            self.chat_frame,
            text=testo,
            bg=colore_bg,
            fg=colore_fg,
            font=("Arial", 13),
            wraplength=600,
            justify="left" if lato == "w" else "right",
            anchor=lato,
            padx=10,
            pady=8,
            bd=1,
            relief="solid"
        )
        nuvoletta.pack(anchor=lato, pady=5, padx=10, fill=None)

        
        self.root.after(100, lambda: self.canvas.yview_moveto(1.0))

    def genera_risposta(self):
        domanda = self.input_box.get("1.0", tk.END).strip()
        if not domanda:
            messagebox.showwarning("Attenzione", "Inserisci una domanda.")
            return
        self.aggiungi_nuvoletta("Tu: " + domanda, "e", "#e0ffe6", "#000000")
        self.input_box.delete("1.0", tk.END)
        self.root.update_idletasks()
        try:
            self.chat_history.append({"role": "user", "content": input})
            self.Temp_chat_history = self.chat_history[:10]
            response = self.client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=self.Temp_chat_history,
                max_tokens=256,
                temperature=0.7,
            )
            self.chat_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
            risposta = response.choices[0].message.content.strip()
        except Exception as e:
            risposta = f"Errore: {e}"
        self.aggiungi_nuvoletta("ChatGPT: " + risposta, "w", "#ffffff", "#222222")



if __name__ == "__main__":
    app = mini_chatGpt()
    app.root.mainloop()
