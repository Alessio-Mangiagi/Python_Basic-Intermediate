"""
Esempio 1: Cos'è un evento in un'interfaccia grafica
Esempio 2: Tipi di eventi in Tkinter
Esempio 3: Il concetto di callback function
"""
import tkinter as tk

def on_button_click():
    print("Hai cliccato il pulsante!")

root = tk.Tk()
root.title("Esempio eventi e callback")

button = tk.Button(root, text="Cliccami", command=on_button_click)
button.pack(padx=20, pady=20)

root.mainloop()
