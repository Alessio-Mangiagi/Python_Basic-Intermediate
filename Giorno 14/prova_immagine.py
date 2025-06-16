import tkinter as tk
from PIL import Image, ImageTk

import sys
import os


def resource_path(relative_path):
    """Restituisce il percorso assoluto per PyInstaller e sviluppo normale."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Mostra immagine")

# Carica l'immagine (deve trovarsi nella stessa cartella del file .py)
img = Image.open(resource_path("Giorno 14\images\charmender.png"))
img_tk = ImageTk.PhotoImage(img)

# Mostra l'immagine in una label
label = tk.Label(root, image=img_tk)
label.pack()

root.mainloop()
