# Importazione delle librerie necessarie
import tkinter as tk
from PIL import Image, ImageTk
import os

class Snake(tk.Canvas):
    """Classe che implementa il gioco Snake con movimento tramite frecce"""
    
    def __init__(self, master=None):
        # Inizializzazione del canvas
        super().__init__(master, bg="white")
        self.pack(fill=tk.BOTH, expand=True)

        try:
            # Percorso dell'immagine
            image_path = os.path.join("Studenti", "Alessio Mangiagi", "icone", "snake.PNG")
            # Caricamento e conversione dell'immagine
            img = Image.open(image_path)
            self.image = ImageTk.PhotoImage(img)
            # Creazione dell'oggetto snake nel canvas
            self.snake = self.create_image(5, 5, image=self.image, anchor=tk.NW, tags="movable")
        except Exception as e:
            # In caso di errore, creare un rettangolo come fallback
            print(f"Errore nel caricamento dell'immagine: {e}")
            self.snake = self.create_rectangle(50, 50, 100, 100, fill="green", tags="movable")

        # Binding degli eventi tastiera
        self.bind("<KeyPress>", self.on_key)
        self.focus_set()

    def sposta(self, dx, dy):
        """Metodo per spostare lo snake nelle coordinate specificate"""
        self.move("movable", dx, dy)

    def on_key(self, event):
        """Gestione degli eventi tastiera per il movimento"""
        dx, dy = 0, 0
        # Definizione dello spostamento in base al tasto premuto
        if event.keysym == "Up":
            dy = -10
        elif event.keysym == "Down":
            dy = 10
        elif event.keysym == "Left":
            dx = -10
        elif event.keysym == "Right":
            dx = 10
        # Esegue lo spostamento
        self.sposta(dx, dy)

# Esecuzione del programma
if __name__ == "__main__":
    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Snake Game")
    root.geometry("1920x1080")
    # Inizializzazione del gioco
    app = Snake(master=root)
    # Avvio del loop principale
    root.mainloop()


