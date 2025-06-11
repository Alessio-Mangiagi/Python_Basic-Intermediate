import tkinter as tk


class MouseEventsApp:
    def __init__(self, root):
        root.title("Esempio Eventi Mouse")

        # Canvas dove disegnare
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        # Label per mostrare le coordinate del mouse
        self.status = tk.Label(root, text="Muovi il mouse sul canvas", anchor="w")
        self.status.pack(fill="x")

        # Bind degli eventi del mouse
        self.canvas.bind("<Button-1>", self.on_left_click)  # clic sinistro
        self.canvas.bind("<Button-3>", self.on_right_click)  # clic destro
        self.canvas.bind("<Motion>", self.on_mouse_move)  # movimento

    def on_left_click(self, event):
        """Disegna un cerchietto rosso di raggio 10px nel punto cliccato."""
        r = 10
        x, y = event.x, event.y
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red", outline="")

    def on_right_click(self, event):
        """Pulisce tutto il canvas."""
        self.canvas.delete("all")

    def on_mouse_move(self, event):
        """Aggiorna la label con le coordinate correnti del mouse."""
        self.status.config(text=f"Mouse: ({event.x}, {event.y})")


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseEventsApp(root)
    root.mainloop()
