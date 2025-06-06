import tkinter as tk
from tkinter import messagebox
import pandas as pd

root = tk.Tk()
root.title("Finestra Tkinter con Sfondo Rosso")
root.configure(bg="red")

def mostra_messaggio():
    messagebox.showinfo("Messaggio", "Hai cliccato il bottone!")

def mostra_csv():
    # Scegli il file CSV da visualizzare
    filename = "\\Users\\lopon\\OneDrive\\Desktop\\Corso Python\\Python_Basic-Intermediate\\studenti\\Antonio Loponte\\viaggi.csv"
    try:
        df = pd.read_csv(filename, delimiter=';')
        # Crea una nuova finestra per la tabella
        win = tk.Toplevel(root)
        win.title("Tabella CSV")
        text = tk.Text(win, width=80, height=20)
        text.pack()
        text.insert(tk.END, df.to_string(index=False))
    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile leggere il file CSV:\n{e}")

btn1 = tk.Button(root, text="Cliccami", bg="white", fg="red", command=mostra_messaggio)
btn1.pack(pady=20)

btn2 = tk.Button(root, text="Chiudi", bg="white", fg="red", command=root.quit)
btn2.pack(pady=20)

btn3 = tk.Button(root, text="Visualizza CSV", bg="white", fg="red", command=mostra_csv)
btn3.pack(pady=20)

root.mainloop()
