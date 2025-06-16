# Importazione delle librerie necessarie
import tkinter as tk              # Per l'interfaccia grafica
from tkinter import messagebox    # Per mostrare messaggi popup
import requests                   # Per le richieste HTTP alle API
from PIL import Image, ImageTk    # Per la gestione delle immagini
from io import BytesIO           # Per gestire i dati binari delle immagini

class SimpleApp:
    def __init__(self):
        # Inizializzazione della finestra principale
        self.root = tk.Tk()                      # Crea la finestra root
        self.root.title("Cagnolino")             # Imposta il titolo
        self.root.geometry("900x500")            # Dimensioni finestra
        self.root.configure(bg="#5BB4EB")        # Colore sfondo
        self.inizializza_sezione_body()          # Chiama il metodo per inizializzare il corpo
        self.root.iconbitmap("Studenti/Alessio Mangiagi/icone/favicon.ico")  # Imposta l'icona
        self.root.mainloop()                     # Avvia il loop principale

    def inizializza_sezione_body(self): 
        # Creazione del frame principale
        self.sezione_body = tk.Frame(self.root, bg="#5BB4EB")
        self.sezione_body.pack(fill=tk.BOTH, expand=True)
        
        # Etichetta del titolo
        self.label = tk.Label(self.sezione_body, text="Cagnolino", 
                            font=("Arial", 24), fg="white", bg="#5BB4EB")
        self.label.pack(pady=20)
        
        # Canvas per mostrare l'immagine
        self.canvas = tk.Canvas(self.sezione_body, bg="white", 
                              width=400, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Frame per i pulsanti
        button_frame = tk.Frame(self.sezione_body, bg="#5BB4EB")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Pulsante per generare frasi
        self.button = tk.Button(button_frame, text="Genera Frase", 
                              font=("Arial", 14), bg="#4a9ed5", fg="white",
                              command=self.genera_frase)
        self.button.pack(side=tk.LEFT, padx=10)
        
        # Pulsante per generare immagini
        self.button2 = tk.Button(button_frame, text="Genera Immagine",
                               font=("Arial", 14), bg="#4a9ed5", fg="white",
                               command=self.img_cane)    
        self.button2.pack(side=tk.LEFT, padx=10)
        
        # Variabile per mantenere il riferimento all'immagine
        self.photo = None
        
    def img_cane(self):
        try:
            # Richiesta all'API per ottenere l'URL di un'immagine casuale di cane
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            if response.status_code == 200:
                img_url = response.json()["message"]
                # Scarica l'immagine dall'URL ottenuto
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # Processa e mostra l'immagine
                    img_data = Image.open(BytesIO(img_response.content))
                    img_data = img_data.resize((380, 280), Image.LANCZOS)
                    self.photo = ImageTk.PhotoImage(img_data)
                    self.canvas.delete("all")
                    self.canvas.create_image(200, 150, image=self.photo, anchor="center")
                else:
                    messagebox.showerror("Errore", "Impossibile scaricare l'immagine.")
            else:
                messagebox.showerror("Errore", "Impossibile ottenere l'URL dell'immagine.")
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {str(e)}")

    def genera_frase(self):
        # Richiesta all'API di Chuck Norris per ottenere una frase casuale
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response.status_code == 200:
            joke = response.json()["value"]
            messagebox.showinfo("Cagnolino", joke)
        else:
            messagebox.showerror("Errore", "Impossibile ottenere il cagnolino.")

# Punto di ingresso dell'applicazione
if __name__ == "__main__":
    app = SimpleApp()            # Crea l'istanza dell'applicazione
    app.root.mainloop()          # Avvia il loop principale

