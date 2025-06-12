import tkinter as tk

class CanvasIntroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Canvas Intro")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)
        self.canvas.pack(pady=30)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CanvasIntroApp()
    app.run()
