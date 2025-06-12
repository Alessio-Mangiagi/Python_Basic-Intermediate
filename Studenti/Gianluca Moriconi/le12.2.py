"""
import tkinter as tk

class Myapp(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.title("MyApp") 
        self.geometry("800x600")
    
        self.frame_body = tk.Frame(self)
        self.frame_body.pack(expand=True)
        
        self.label = tk.Label(self.frame_body, text="Benvenuto")
        self.label.pack(pady=20)

        self.printbutton = tk.Button(self.frame_body, text="Clicca", padx=10, pady=10, background="orange", command=self.on_button_click)
        self.printbutton.pack()

    def on_button_click(self):
        self.label.config(text="Hai premuto il pulsante")
        

if __name__ == "__main__":
    app = Myapp()
    app.mainloop()
"""
#----------------------------------------------------------------------------------------

"""
#Esempio 1: Cos'è un evento in un'interfaccia grafica
#Esempio 2: Tipi di eventi in Tkinter
#Esempio 3: Il concetto di callback function

import tkinter as tk

def on_button_click():
    print("Hai cliccato il pulsante!")

root = tk.Tk()
root.title("Esempio eventi e callback")

button = tk.Button(root, text="Cliccami", command=on_button_click)
button.pack(padx=20, pady=20)

root.mainloop()
"""

#----------------------------------------------------------------------------------------

"""
#Esempio 4: Il metodo bind() per associare eventi
#Esempio 5: Eventi da tastiera: <KeyPress>, <Return>
#Esempio 6: Eventi da mouse: <Button-1>, <Double-Button-1>

import tkinter as tk

def on_key(event):
    print(f"Tasto premuto: {event.keysym}")

def on_click(event):
    print(f"Click con il mouse alle coordinate: {event.x}, {event.y}")

root = tk.Tk()
root.title("Esempio bind eventi")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)
entry.bind("<KeyPress>", on_key)
entry.bind("<Return>", lambda e: print("Invio premuto!"))

root.bind("<Button-1>", on_click)
root.bind("<Double-Button-1>", lambda e: print("Doppio click!"))

root.mainloop()
"""

#----------------------------------------------------------------------------------------

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
