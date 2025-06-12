import tkinter as tk

class Myapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("800x600")
        
        self.frame_body = tk.Frame(self)
        self.frame_body.pack(expand=True)

        self.label = tk.Label(self.frame_body, text="Benvenuto")
        self.label.pack(pady=20)

        self.printbutton = tk.Button(self.frame_body, text="Clicca", padx=10, pady=10, bg="orange")
        self.printbutton.pack() 
        self.printbutton.bind("<Button-1>", lambda event: self.on_button_click(event))



    def click_pulsante(self):
        self.label.config(text="Hai cliccato").pack()

    def on_button_click(self, event):
        print(f"Hai cliccato alle coordinate x={event.x}, y={event.y}")
        

if __name__ == "__main__":
    app = Myapp()
    app.mainloop()

