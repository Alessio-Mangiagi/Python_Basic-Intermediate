import tkinter as tk
import requests

class CagnolinoGenerator:
    def __init__(self):
        self.title("Cagnolino Generator")
        self.geometry("800x600")
                
        self.inizializza_sezione_body()
        
    def inizializza_sezione_body(self):
        self.body = tk.Frame(self)
        self.body.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.body, text="Cagnolino Generator")
        self.label.pack(pady=10, padx=10, anchor=tk.CENTER)
        
        self.canvas = tk.Canvas(self.body, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.button = tk.Button(self.body, text="Genera Cagnolino", command=self.genera_cagnolino)
        self.button.pack()

root = tk.Tk()
App = CagnolinoGenerator(root)
root.mainloop()