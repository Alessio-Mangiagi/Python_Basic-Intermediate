import tkinter as tk
from tkinter import messagebox  

Fuel_type = {
    "Benzina": 1.5,
    "Diesel": 1.4,
    "GPL": 0.8,
    "Metano": 0.9
}   

def inserimento(valore):
    controllo = valore.get()
    if not controllo:
        messagebox.showerror("Errore", "Inserisci un valore.")
        return None
    try:
        return float(valore)
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un valore numerico.")
        return None

class FuelCalculator:
    def __init__(self):
        
        def inserimento(valore):
            controllo = valore.get()
            if not controllo:
                messagebox.showerror("Errore", "Inserisci un valore.")
                return None
            try:
                return float(valore)
            except ValueError:
                messagebox.showerror("Errore", "Inserisci un valore numerico.")
                return None
            
        self.window = tk.Tk()
        self.window.title("Calcolo del consumo di combustibile")
        vcmd = (self.window.register(self.validate_input), '%P')
        self.window.geometry("600x400")
        self.window.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
        self.window.iconbitmap("Studenti/Alessio Mangiagi/icone/favicon.ico")
        self.create_widgets()
        
    label = tk.Label(self.window, text="distanza percorsa", bg="#3653D1", fg="white", font=("Arial", 24))
    label.pack(pady=20)
    

        
    