from tkinter import *

# Funzione che gestisce l'evento del mouse
def doSomething(event):
    print("Coordinate del mouse: x =", event.x, "y =", event.y)

# Altri eventi del mouse che potresti voler gestire
"""def doSomething2(event):
    print("Hai fatto qualcosa con il mouse! (rotellina)")

def doSomething3(event):
    print("Hai fatto qualcosa con il mouse! (tasto destro)")  """  

# Creazione della finestra principale
window = Tk()
window.geometry("800x600")  # Imposta le dimensioni della finestra
window.title("Evento mouse")


# Imposta le dimensioni della finestra

window.bind("<Button-1>",doSomething)
"""window.bind("<Button-2>",doSomething2)
window.bind("<Button-3>",doSomething3)"""

window.mainloop()