import tkinter as tk

class myapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("interfaccia utente")
        self.geometry("500x500")
        self.config(bg="#ffffff") 
        self.iconbitmap="Studenti\\Alessio Mangiagi\\icone\\favicon.ico"
        
        self.frame_body = tk.Frame(self)  # Frame con la F maiuscola
        self.frame_body.pack()
        
        self.label = tk.Label(self, text="tette", bg="#ffffff")
        self.label.pack(side="top", pady=30)
        
        self.button = tk.Button(self.frame_body, text="click", bg="#ff00e6", fg="#000000", font=("Arial", 24), command=self.click_Button)
        self.button.pack(side="left")
        
        self.printbutton = tk.Button(self.frame_body, text="print",bg="#ff00e6", fg="#000000", font=("Arial", 24))
        self.printbutton.pack(side="right")    
    def click_Button(self):
        """Crea una label con il testo "Benvenuto!" e la pone sopra il bottone"""
        self.label = tk.Label(self.frame_body, text="Benvenuto!", bg="#ffffff")
        self.label.pack(side="top")
    
    
if __name__=="__main__":
    app = myapp()
    app.mainloop()