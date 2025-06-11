"""
Esempio 7: Eventi di movimento del mouse
Esempio 8: Passaggio dell’evento alla funzione
Esempio 9: event.x, event.y: coordinate del click
Esempio 5: Eventi da tastiera (<KeyPress>, <Return>)
Esempio 6: Eventi da mouse (<Button-1>, <Double-Button-1>)
Esempio 12: Eventi su Entry e Text
Esempio 14: Uso di lambda per passare parametri
"""
import tkinter as tk

# Movimento mouse su una label

def on_motion(event):
    label.config(text=f"Mouse a: {event.x}, {event.y}")

# Eventi da tastiera su Entry

def on_keypress(event):
    info_label.config(text=f"Tasto premuto: {event.keysym}")

def on_return(event):
    info_label.config(text="Hai premuto Invio nell'Entry!")

# Eventi da mouse su tutta la finestra

def on_click(event):
    info_label.config(text=f"Click a ({event.x}, {event.y})")

def on_double_click(event):
    info_label.config(text=f"Doppio click a ({event.x}, {event.y})")

# Evento su Text

def on_text_focus(event):
    info_label.config(text="Text in focus!")

root = tk.Tk()
root.title("Esempi eventi vari")

label = tk.Label(root, text="Muovi il mouse qui sopra", width=30, height=3, bg="lightgray")
label.pack(padx=10, pady=5)
label.bind("<Motion>", on_motion)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5)
entry.bind("<KeyPress>", on_keypress)
entry.bind("<Return>", on_return)

text = tk.Text(root, height=2, width=30)
text.pack(padx=10, pady=5)
text.bind("<FocusIn>", on_text_focus)

# Uso di lambda per passare parametri a una callback
btn = tk.Button(root, text="Mostra messaggio", command=lambda: info_label.config(text="Hai premuto il bottone! (lambda)"))
btn.pack(padx=10, pady=5)

# Bind eventi mouse sulla finestra
root.bind("<Button-1>", on_click)
root.bind("<Double-Button-1>", on_double_click)

info_label = tk.Label(root, text="Info eventi", fg="blue")
info_label.pack(padx=10, pady=10)

root.mainloop()
