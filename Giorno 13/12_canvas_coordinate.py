import tkinter as tk

class CanvasCoordinateApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Canvas Coordinate")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)
        self.canvas.pack(pady=30)
        # Mostra le coordinate di alcuni punti
        self.canvas.create_text(60, 10, text="(60,20)")
        self.canvas.create_oval(55, 15, 65, 25, fill="red")
        self.canvas.create_text(200, 90, text="(200,100)")
        self.canvas.create_oval(195, 95, 205, 105, fill="blue")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CanvasCoordinateApp()
    app.run()
