from openai import OpenAI
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import messagebox

class skynet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("skynet")
        self.root.geometry("900x800")
        load_dotenv() 
        self.client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
        )
        self.interfaccia()


    def interfaccia(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.inserisci_testo = tk.Text(self.frame, wrap=tk.WORD)
        self.inserisci_testo.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.inserisci_testo_bottone = tk.Button(self.frame, text="Riassumi", command=self.riassumi_testo)
        self.inserisci_testo_bottone.pack(pady=10)
        self.correzione_bottone = tk.Button(self.frame, text="Correggi", command=self.correggi_testo)
        self.correzione_bottone.pack(pady=10)
        self.testo_riassunto = tk.Text(self.frame, wrap=tk.WORD)
        self.testo_riassunto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.testo_riassunto.insert(tk.END, "La risposta apparirà qui")

    def riassumi_testo(self):
        testo = self.inserisci_testo.get("1.0", tk.END).strip()
        if not testo:
            messagebox.showwarning("Attenzione", "Inserisci del testo da riassumere.")
            return
        try:
            risposta = self.chiamata_openai(message=f"Riassumi il seguente testo: {testo}")
            riassunto = risposta.choices[0].message.content.strip()
            self.testo_riassunto.delete("1.0", tk.END)
            self.testo_riassunto.insert(tk.END, riassunto)
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")
            return

    def correggi_testo(self):
        testo = self.inserisci_testo.get("1.0", tk.END).strip()
        if not testo:
            messagebox.showwarning("Attenzione", "Inserisci del testo da correggere.")
            return
        try:
            risposta = self.chiamata_openai(message=f"Correggi la grammatica del testo inserito: {testo}, senza spiegazioni riportami solo il testo corretto.")
            testo_corretto = risposta.choices[0].message.content.strip()
            self.testo_riassunto.delete("1.0", tk.END)
            self.testo_riassunto.insert(tk.END, testo_corretto)
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")
            return


        

        

    def chiamata_openai(self, model="gpt-4.1-nano", message=""):
        risposta = self.client.chat.completions.create(
            model = model,
            messages=[
                {"role": "user", "content": message}]
            )
        return risposta


if __name__ == "__main__":
    app = skynet()
    risposta = app.chiamata_openai(message="Genera un numero pari tra 1 e 100")
    app.root.mainloop()
