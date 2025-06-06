import tkinter as tk

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

label = tk.Label(center_frame, text="Non hai ancora premuto il pulsante...", bg="#404040", fg="orange", font=("Arial", 20, "bold"))
label.pack(pady=20)

pulsante = tk.Button(center_frame, text="Clicca!", bg="#FFC400", command=n_clicks, font=("Arial", 20, "bold"))
pulsante.pack(pady=10)

root.mainloop() #avvio schermata (A FINE CODICE)