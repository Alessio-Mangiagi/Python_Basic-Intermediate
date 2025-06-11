import tkinter as tk

class Myapp(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.title("MyApp") 
        self.geometry("800x600")
    
        self.frame_body = tk.Frame(self)
        self.frame_body.pack(expand=True)
        
        self.label = tk.Label(self.frame_body, text="Benvenuto")
        self.label.pack(pady=20)

        self.printbutton = tk.Button(self.frame_body, text="Clicca", padx=10, pady=10, background="orange", command=self.click_pulsante)
        self.printbutton.pack()

    def click_pulsante(self):
        self.label.config(text="Hai premuto il pulsante")
        

if __name__ == "__main__":
    app = Myapp()
    app.mainloop()