import tkinter as tk
import random

root = tk.Tk()
root.title("bottoni rosso")
root.geometry("900x500")

canvas = tk.Canvas(root, width=900, height=500, bg="white")
canvas.pack()

for i in range(10): # 10 righe
    color = "#E40E1A" if i % 2 == 0 else "#08ADE9"
    canvas.create_rectangle(0, i * 50, 900, (i + 1) * 50, fill=color, outline="")
    
# Variabile globale per contare i click
click = 0

def incrementa_click():
    global click
    click += 1
    label.config(text=f"sei catanese {click} volte")
label = tk.Label(root, text=(f"sei catanese {click} volte"), bg="#0e0ee4", fg="white")

#bottoni
button1 = tk.Button(root, text="FORZA CATANIA!!!", bg="#e40e1a", fg="white", command=incrementa_click)
#stile del bottone
button1.config(font=("Helvetica", 16, "bold"))


canvas.create_window(450, 250, window=label)
canvas.create_window(450, 350, window=button1)


root.mainloop()