import tkinter as tk

class AppEsercitazione(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Esercitazione Eventi e Callback")
        self.geometry("600x400")
        self.inizializza_ui()

    def inizializza_ui(self):
        """Inizializza l'interfaccia utente."""
        # Creazione di un frame per i bottoni
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        # Creazione di un bottone
        button = tk.Button(button_frame, text="Cliccami", command=self.on_button_click)
        button.pack(pady=10)

        # Creazione label per visualizzare il testo
        self.label = tk.Label(self, text="Clicca il bottone per vedere l'azione", font=("Arial", 14))
        self.label.pack(pady=20)

    def on_button_click(self):
        """Callback per il click del bottone."""
        print("Bottone cliccato!")
        self.label.config(text="Hai cliccato il bottone!")

# Avvio dell'applicazione
if __name__ == "__main__":
    app = AppEsercitazione()
    app.mainloop()