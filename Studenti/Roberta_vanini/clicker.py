import tkinter as tk
from PIL import Image, ImageTk

# creazione finestra

root = tk.Tk()
root.title("Clicker")   #diamogli un titolo
root.geometry("800x600")            #stabiliamo le dimensioni
root.resizable(False, False)        #per non permettere il resize della finestra
root.configure(bg="#404040")     #per colorare lo sfondo

# creazione di un frame al centro
center_frame = tk.Frame(root, bg="#404040")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

counter = 0

def n_clicks():
    global counter
    counter += 1
    label.config(text=f"Hai premuto il bottone {counter} volte!")

# img bottone
button_img = ImageTk.PhotoImage(Image.open("Python_Basic-Intermediate/Studenti/Roberta_vanini/button.png"))

label = tk.Label(center_frame, text="Non hai ancora premuto il pulsante...", bg="#404040", fg="orange", font=("Arial", 20, "bold"))
label.pack(pady=20)

pulsante = tk.Button(center_frame, image = button_img , border= 0, background="#404040",  command=n_clicks)
pulsante.pack(pady=10)

root.mainloop() #avvio schermata (A FINE CODICE)