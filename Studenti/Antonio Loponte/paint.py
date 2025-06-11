import tkinter as tk


class SempliceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Paint cinese")
        self.geometry("800x600")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.last = [0, 0]
        self._bind_events()

    def start_draw(self, event):
        self.last = [event.x, event.y]

    def draw(self, event):
        x, y = event.x, event.y
        if self.last != [0, 0]:
            self.canvas.create_line(self.last[0], self.last[1], x, y, fill="black", width=2)
        self.last = [x, y]

    def _bind_events(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)


app = SempliceApp()
app.mainloop()