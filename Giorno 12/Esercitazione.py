import tkinter as tk


class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Tkinter App")
        self.geometry("600x600")
        self.Initialize_toolbar()
        self.Initialiaze_Body()
        self._bind_events()
        self.last = [0, 0]
        self.line_width = 1

    def clear(self):
        """Clear the content of the application."""
        print("Clear button clicked")

    def show_info(self):
        """Show information about the application."""
        print("Info: This is a simple Tkinter application.")

    def Enter_Callback(self, event, color="lightblue"):
        """Callback for mouse entering a widget."""
        print("Mouse entered widget:", event.widget)
        event.widget.config(bg=color)

    def Leave_Callback(self, event, color="lightgray"):
        """Callback for mouse leaving a widget."""
        print("Mouse left widget:", event.widget)
        event.widget.config(bg=color)

    def start_drawing(self, event):
        self.last = [event.x, event.y]

    def draw(self, event, mode="draw"):
        """Draw on the canvas when the mouse is moved."""
        x, y = event.x, event.y
        if self.last != [0, 0]:
            if mode == "draw":
                self.canvas.create_line(
                    self.last[0],
                    self.last[1],
                    x,
                    y,
                    fill="black",
                    width=self.line_width,
                )
            else:
                self.canvas.create_line(
                    self.last[0],
                    self.last[1],
                    x,
                    y,
                    fill=self.canvas["bg"],
                    width=self.line_width + 5,
                )
        self.last = [x, y]

    def active_drawing(self):
        self.canvas.bind("<B1-Motion>", lambda e: self.draw(e, "draw"))

    def active_erase(self):
        self.canvas.bind("<B1-Motion>", lambda e: self.draw(e, "erase"))

    def Increase_size(self, event):
        """Increase the size of the drawing."""
        self.line_width += 1
        print(f"Line width increased to {self.line_width}")

    def Decrease_size(self, event):
        """Decrease the size of the drawing."""
        if self.line_width > 1:
            self.line_width -= 1
            print(f"Line width decreased to {self.line_width}")
        else:
            print("Line width cannot be decreased further")

    def Initialize_toolbar(self):
        """Initialize the application."""
        self.toolbar = tk.Frame(self, bg="lightgray", bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.button_clear = tk.Button(self.toolbar, text="Clear", command=self.clear)
        self.button_clear.pack(side=tk.LEFT, padx=2, pady=2)

        self.button_info = tk.Button(self.toolbar, text="Info", command=self.show_info)
        self.button_info.pack(side=tk.LEFT, padx=2, pady=2)

    def initialize_tool_disegno(self):
        """Initialize the drawing tools."""
        self.tool_frame = tk.Frame(self.body_frame, bg="lightgray")
        self.tool_frame.pack(side=tk.LEFT, padx=2, pady=2, anchor="n")

        self.button_matita = tk.Button(
            self.tool_frame,
            text="Matita",
            command=self.active_drawing,
        )
        self.button_matita.pack(padx=2, pady=2, side=tk.TOP)

        self.button_gomma = tk.Button(
            self.tool_frame,
            text="Gomma",
            command=self.active_erase,
        )
        self.button_gomma.pack(padx=2, pady=2, side=tk.TOP)

    def Initialiaze_Body(self):
        """Create the main body of the application."""
        self.body_frame = tk.Frame(self)
        self.body_frame.pack(fill=tk.BOTH, expand=True)
        self.label = tk.Label(
            self.body_frame,
            text="Disegna quello che vuoi",
            anchor="center",
            justify=tk.CENTER,
        )
        self.label.pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

        self.initialize_tool_disegno()
        self.canvas = tk.Canvas(self.body_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def _bind_events(self):
        """Bind events to the application."""
        self.button_info.bind("<Enter>", lambda e: self.Enter_Callback(e, "lightblue"))
        self.button_info.bind("<Leave>", lambda e: self.Leave_Callback(e, "lightgray"))
        self.button_clear.bind("<Enter>", lambda e: self.Enter_Callback(e, "lightblue"))
        self.button_clear.bind("<Leave>", lambda e: self.Leave_Callback(e, "lightgray"))
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<Button-2>", self.Increase_size)
        self.canvas.bind("<Button-3>", self.Decrease_size)


app = SimpleApp()
app.mainloop()
