import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox

# Creazione della finestra
root=tk.Tk()
root.title("ciao")
root.geometry("900x400")
root.configure(bg="blue")

# Funzione per mostrare un messaggio quando il pulsante viene cliccato
def show_message():
    messagebox.showinfo("Informazione", "Ciao, questo è un messaggio di prova!")
    info_label = tk.Label(root, text="Ciao, questo è un messaggio di prova!", bg="pink", fg="white")
    info_label.pack(pady=20)

   
def create_window():
    window = tk.Tk()
    window.title("Prova Tkinter")
    window.geometry("600x200")
    
    # Imposta il font
    custom_font = font.Font(family="Helvetica", size=12, weight="bold")
    
    # Crea un pulsante con il font personalizzato
    button = tk.Button(window, text="Clicca qui", command=show_message, font=custom_font)
    button.pack(pady=20)
    
    window.mainloop()
 
root.mainloop()
show_message()