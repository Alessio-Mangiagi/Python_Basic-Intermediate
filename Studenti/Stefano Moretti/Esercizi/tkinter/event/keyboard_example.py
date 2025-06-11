from tkinter import *
ù
# Funzione che gestisce l'evento della pressione di un tasto
def doSomething(event):
    print("Hai premuto: " + event.keysym) # Stampa il nome del tasto premuto
    label.config(text=event.keysym) 

# Creazione della finestra principale
window = Tk()
window.title("Keyboard Event Example")
window.geometry("800x600")

# Associa la funzione doSomething all'evento di pressione di un tasto
window.bind("<Key>",doSomething)

# Etichetta per visualizzare il tasto premuto
label = Label(window,font=("Helvetica", 100))
label.pack()

window.mainloop()