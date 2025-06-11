import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        root.title("Gestione KeyPress con bind")

        # Creiamo un Canvas e un rettangolo al centro
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()
        # Rettangolo iniziale
        self.rect = self.canvas.create_rectangle(180, 130, 220, 170, fill="blue")

        # Bind dell'evento KeyPress su tutto il widget root
        # Ogni volta che l'utente preme un tasto, viene chiamato il metodo on_key
        root.bind("<KeyPress>", self.on_key)

    def on_key(self, event):
        """Callback per la pressione di un tasto."""
        key = event.keysym  # nome simbolico del tasto (es. 'Left', 'a', 'Return', ...)
        dx, dy = 0, 0

        if key == "Left":
            dx = -10
        elif key == "Right":
            dx = 10
        elif key == "Up":
            dy = -10
        elif key == "Down":
            dy = 10
        elif key.lower() == "r":
            # Ripristina la posizione iniziale
            self.canvas.coords(self.rect, 180, 130, 220, 170)
            return
        else:
            print(f"Hai premuto: {key!r}")
            return

        # Sposta il rettangolo
        self.canvas.move(self.rect, dx, dy)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
