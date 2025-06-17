import tkinter as tk
import requests
from PIL import Image, ImageTk    # Per la gestione delle immagini
from io import BytesIO           # Per gestire i dati binari delle immagini


class CagnolinoGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cagnolino Generator")
        self.root.geometry("800x600")
        self.ALTEZZA_CANVAS = 600
        self.LARGHEZZA_CANVAS = 800
        self.inizializza_sezione_body()
        self.root.mainloop()                     # Avvia il loop principale

    def inizializza_sezione_body(self):
        self.body = tk.Frame(self.root)
        self.body.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.body, text="Cagnolino Generator")
        self.label.pack(pady=10, padx=10, anchor=tk.CENTER)
        
        self.button = tk.Button(self.body, text="Genera Cagnolino", command=self.genera_cagnolino)
        self.button.pack()
        
        self.canvas = tk.Canvas(self.body, width=self.LARGHEZZA_CANVAS, height=self.ALTEZZA_CANVAS)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
    def genera_cagnolino(self):
        #! Esempio di richiesta API
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            response.raise_for_status()
            img_url = response.json()["message"]
            img_data = requests.get(img_url).content
            img = Image.open(BytesIO(img_data))
            img = img.resize((self.ALTEZZA_CANVAS, self.LARGHEZZA_CANVAS), Image.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(img)
            self.canvas.delete("all")
            self.canvas.create_image(self.LARGHEZZA_CANVAS/2, self.ALTEZZA_CANVAS/2, image=self.img_tk)

        except Exception as e:
            print("Errore nel caricamento dell'immagine")

app = CagnolinoGenerator()
app.root.mainloop()