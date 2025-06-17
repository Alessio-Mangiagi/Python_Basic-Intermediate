import tkinter as tk
from tkinter import messagebox
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Stampa un messaggio di benvenuto decorativo
print("><(((º> sabusabu <º)))><")


class skynet:
    def __init__(self):
        # Inizializza la finestra principale di tkinter
        self.root = tk.Tk()
        self.root.title("skynet")
        self.root.geometry("900x800")

        # Imposta l'icona della finestra (nota: il percorso potrebbe non funzionare)
        self.rooticonbitmap = tk.PhotoImage(
            file="Studenti\\Alessio Mangiagi\\icone\\snake.PNG"
        )

        # Imposta il colore di sfondo della finestra
        self.root.config(bg="#000000")

        # Chiama il metodo per creare l'interfaccia
        self.pagina()

        # Inizializza la cronologia della chat con un messaggio di sistema
        self.chat_history = [
            {
                "role": "system",
                "content": "Al primo messaggio chiedi sempre all'utente di presentarsi e di dire qualcosa su di lui.",
            },
        ]

    def pagina(self):
        # Crea il container principale per tutti gli elementi dell'interfaccia
        self.container = tk.Frame(self.root)

        # Crea l'area di testo per visualizzare la conversazione
        self.continar_testo = tk.Text(self.container)

        # Posiziona gli elementi nell'interfaccia
        self.container.pack()
        self.continar_testo.pack()

        # Crea il campo di input per l'utente
        self.imput_testo = tk.Entry(self.container)
        self.imput_testo.pack(fill=tk.X, padx=10, pady=10)

        # Crea il pulsante per inviare messaggi
        self.button = tk.Button(
            self.container,
            text="invia",
            bg="#767bbc",
            fg="#000000",
            font=("Arial", 24),
            command=self.click_Button,
        )
        self.button.pack()

        # Crea il pulsante per salvare la chat
        self.button_save_log = tk.Button(
            self.container,
            text="Salva chat",
            bg="#767bbc",
            fg="#000000",
            font=("Arial", 24),
            command=self.save_chat_in_test_file,
        )
        self.button_save_log.pack(pady=10)

    def click_Button(self):
        # Ottiene il testo inserito dall'utente
        self.imput_utente = self.imput_testo.get()

        # Pulisce il campo di input
        self.imput_testo.delete(0, tk.END)

        # Aggiunge il messaggio dell'utente all'area di testo
        self.continar_testo.insert(tk.END, f" Utente:{self.imput_utente}\n")

        # Chiama OpenAI e aggiunge la risposta all'area di testo
        self.continar_testo.insert(
            tk.END, f" SkyNet:{self.ask_openai(self.imput_utente)}\n"
        )

        # Associa il tasto Enter al pulsante di invio
        self.imput_testo.bind("<Return>", lambda event: self.click_Button())

        # Riporta il focus sul campo di input
        self.imput_testo.focus_set()

    def ask_openai(self, input):
        # Crea il client OpenAI usando la chiave API dalle variabili d'ambiente
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        # Aggiunge il messaggio dell'utente alla cronologia
        self.chat_history.append({"role": "user", "content": input})

        # Mantiene solo gli ultimi 10 messaggi per limitare il contesto
        self.Temp_chat_history = self.chat_history[:10]

        # Effettua la chiamata all'API OpenAI
        completion = client.chat.completions.create(
            model="gpt-4.1-nano",
            store=True,
            messages=self.Temp_chat_history,
        )

        # Estrae la risposta dall'API
        openai_response = completion.choices[0].message.content.strip()

        # Aggiunge la risposta dell'assistente alla cronologia
        self.chat_history.append({"role": "assistant", "content": openai_response})

        return openai_response

    def save_chat_in_test_file(self):
        # Salva la cronologia della chat in un file di testo
        with open("chat_history.txt", "w") as file:
            for message in self.chat_history:
                # Salta i messaggi di sistema
                if message["role"] == "system":
                    pass
                else:
                    role = message["role"]
                    content = message["content"]
                    file.write(f"{role}: {content}\n")

        # Mostra un messaggio di conferma del salvataggio
        messagebox.showinfo(
            "Salvataggio", "La chat è stata salvata in chat_history.txt"
        )


# Verifica se il file viene eseguito direttamente
if __name__ == "__main__":
    # Crea un'istanza dell'applicazione e avvia il loop principale di tkinter
    app = skynet()
    app.root.mainloop()
