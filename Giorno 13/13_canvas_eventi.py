import tkinter as tk

class CanvasEventiApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Canvas Eventi di Disegno")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)
        self.canvas.pack(pady=30)
        self.canvas.bind("<B1-Motion>", self.disegna)
        self.last_x = None
        self.last_y = None
    def disegna(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill="black")
        self.last_x = event.x
        self.last_y = event.y
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CanvasEventiApp()
    app.run()
