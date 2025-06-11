import tkinter as tk
from PIL import Image, ImageTk
'''da sistemare le immagini, non funzionano, ma il codice è corretto'''
# Codice per un gioco Snake semplice con immagini e movimento con le frecce della tastiera
class Snake(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.pack(fill=tk.BOTH, expand=True)

        # Carica immagine
        img = Image.open("Studenti\\Alessio Mangiagi\\icone\\snake.PNG")  # Usa anche .gif se è statica
        self.image = ImageTk.PhotoImage(img)
        
        # Aggiungi immagine al canvas
        self.snake = self.create_image(50, 50, image=self.image, anchor=tk.NW, tags="movable")

        self.bind("<KeyPress>", self.on_key)
        self.focus_set()

    def sposta(self, dx, dy):
        self.move("movable", dx, dy)

    def on_key(self, event):
        dx, dy = 0, 0
        if event.keysym == "Up":
            dy = -10
        elif event.keysym == "Down":
            dy = 10
        elif event.keysym == "Left":
            dx = -10
        elif event.keysym == "Right":
            dx = 10
        self.sposta(dx, dy)

if __name__ == "__main__":  
    root = tk.Tk()
    root.title("Snake Game")   
    root.geometry("900x500")
    app = Snake(master=root)        
    root.mainloop()


