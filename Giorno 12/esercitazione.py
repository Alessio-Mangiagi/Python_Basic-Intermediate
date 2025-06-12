import tkinter as tk
from tkinter import messagebox

# L'esercizio prevede una mini-app che permette di inserire il proprio nome, cliccare un bottone oppure premere Invio per mostrare un saluto,
# e passare il mouse sopra la label per cambiarne il colore.


class App(tk.Tk):
    def __init__(self):
        # Inizializza la finestra principale
        super().__init__()
        self.title("Esercitazione 12")  # Imposta il titolo della finestra
        self.geometry("800x600")  # Imposta le dimensioni della finestra

        # Crea la label per l'istruzione di inserimento nome
        self.label_nome = tk.Label(self, text="Inserisci il tuo nome:")
        self.label_nome.pack(pady=10)  # Posiziona la label con padding verticale

        # Inizializza i contatori per i bottoni e i cambi di colore
        self.button_counter = 0
        self.color_counter = 0

        # Crea il campo di input per il nome
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=10)

        # Crea il bottone per il saluto
        self.button_saluto = tk.Button(self, text="Saluto", command=self.mostra_saluto)
        self.button_saluto.pack(pady=10)
        # Associa il tasto Invio al metodo mostra_saluto
        self.entry_nome.bind("<Return>", lambda e: self.mostra_saluto())

        # Variabile per la checkbox del saluto formale
        self.checkbox_saluto = tk.BooleanVar()

        # Crea la checkbox per il saluto formale
        self.checkbox = tk.Checkbutton(
            self,
            text="Mostra saluto formale",
            variable=self.checkbox_saluto,
        )
        self.checkbox.pack(pady=10)

        # Variabile per i radiobutton dei colori (default: blue)
        self.radiobutton_saluti = tk.StringVar(value="blue")

        # Crea i radiobutton per selezionare i colori
        self.radiobutton_rosso = tk.Radiobutton(
            self, text="rosso", variable=self.radiobutton_saluti, value="red"
        )
        self.radiobutton_rosso.pack(pady=5)

        self.radiobutton_verde = tk.Radiobutton(
            self, text="verde", variable=self.radiobutton_saluti, value="green"
        )
        self.radiobutton_verde.pack(pady=5)

        self.radiobutton_blu = tk.Radiobutton(
            self, text="blu", variable=self.radiobutton_saluti, value="blue"
        )
        self.radiobutton_blu.pack(pady=5)

        # Crea le label per mostrare i contatori
        self.label_counter_button = tk.Label(
            self, text="Button counter: " + str(self.button_counter)
        )
        self.label_color_counter = tk.Label(
            self, text="Color counter: " + str(self.color_counter)
        )
        self.label_counter_button.pack(pady=10)
        self.label_color_counter.pack(pady=10)

        # Crea il bottone per il reset
        self.label_reset = tk.Button(self, text="Reset", command=self.reset)
        self.label_reset.pack(pady=10)

        # Flag per gestire il doppio click
        self.double_click = False

    def mostra_saluto(self):
        # Prova a distruggere la label del saluto precedente se esiste
        try:
            if self.label_saluto:
                self.label_saluto.destroy()
        except Exception as e:
            messagebox.showwarning("Attenzione", f"La label saluto non esiste: {e}")

        # Incrementa il contatore dei bottoni e aggiorna la label
        self.button_counter += 1
        self.label_counter_button.config(
            text="Counter button: " + str(self.button_counter)
        )

        # Ottiene il nome dall'entry
        nome = self.entry_nome.get()

        # Crea la label del saluto in base allo stato della checkbox
        if self.checkbox_saluto.get():
            self.label_saluto = tk.Label(self, text=f"Ciao {nome}!")
        else:
            self.label_saluto = tk.Label(self, text=f"Non ti saluto {nome}!")

        self.label_saluto.pack(pady=10)

        # Associa gli eventi alla label del saluto
        # Quando il mouse entra, cambia colore secondo il radiobutton selezionato
        self.label_saluto.bind(
            "<Enter>", lambda e: self.cambia_colore(e, self.radiobutton_saluti.get())
        )
        # Quando il mouse esce, torna al colore nero
        self.label_saluto.bind("<Leave>", self.cambia_colore)
        # Quando si fa doppio click, cambia il testo
        self.label_saluto.bind("<Double-Button-1>", self.cambia_testo)

    def cambia_colore(self, event, colore="black"):
        # Cambia il colore del testo della label del saluto
        self.label_saluto.config(fg=colore)
        # Incrementa il contatore dei cambi di colore e aggiorna la label
        self.color_counter += 1
        self.label_color_counter.config(
            text="Color counter: " + str(self.color_counter)
        )

    def reset(self):
        # Prova a distruggere la label del saluto se esiste
        try:
            if self.label_saluto:
                self.label_saluto.destroy()
        except Exception as e:
            messagebox.showerror(
                "Errore", f"Si è verificato un errore durante il reset: {e}"
            )

        # Resetta i contatori
        self.button_counter = 0
        self.color_counter = 0

        # Aggiorna le label dei contatori
        self.label_counter_button.config(
            text="Button counter: " + str(self.button_counter)
        )
        self.label_color_counter.config(
            text="Color counter: " + str(self.color_counter)
        )

    def cambia_testo(self, event):
        try:
            # Se non è stato ancora fatto un doppio click
            if not self.double_click:
                if self.label_saluto:
                    # Cambia il testo per indicare il doppio click
                    self.label_saluto.config(text="Hai fatto doppio click!")
                    self.double_click = True
                else:
                    print("La label saluto non esiste.")
            else:
                # Se è già stato fatto un doppio click, ripristina il testo originale
                if self.checkbox_saluto.get():
                    self.label_saluto.config(text=f"Ciao {self.entry_nome.get()}!")
                else:
                    self.label_saluto.config(
                        text=f"Non ti saluto {self.entry_nome.get()}!"
                    )
                self.double_click = False
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")


# Crea un'istanza dell'applicazione e avvia il loop principale
instanza_app = App()
instanza_app.mainloop()
