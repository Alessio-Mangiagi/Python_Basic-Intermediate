import tkinter as tk
from tkinter import *

"""
root = tk.Tk()
root.title("Prova bottoni")
root.geometry("900x500")
root.configure(bg="#1f1f1f")   
        
canvas = tk.Canvas(root, width=900, height=500)
canvas.pack()

for i in range(10):
    color = "#1f1f1f" if i % 2 == 0 else "#2f2f2f"  # Colori alternati
    canvas.create_rectangle(0, i * 50, 900, (i + 1) * 50, fill=color, outline="")

click = 0  # Variabile per contare i click

def click_counter():
    global click
    click += 1
    label.config(text=f"Prova bottoni {click} volte") 


label = tk.Label(root, text=(f"Prova bottoni {click} volte"), bg="#1f1f1f", fg="white")



#bottoni
button1 = Button(root, text="Button 1", command = click_counter, bg="#EC4807", fg="white")
#stile del bottone
button1.config(font=("helvetica", 12, "bold"))

canvas.create_window(450, 200, window=label)  # Posizione dell'etichetta al centro del canvas
canvas.create_window(450, 250, window=button1)  # Posizione del bottone al centro del canvas


root.mainloop()

"""

 