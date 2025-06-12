import tkinter as tk


class CanvasDisegnoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Canvas Disegno Forme")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)
        self.canvas.pack(pady=30)
        # Disegno di una linea
        self.canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
        # Disegno di un rettangolo
        self.canvas.create_rectangle(20, 40, 120, 100, outline="red", width=2)
        self.canvas.create_oval(20, 40, 120, 100, outline="green", width=2)
        # Disegno di un ovale
        self.canvas.create_oval(150, 50, 250, 120, outline="green", width=2)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CanvasDisegnoApp()
    app.run()
