# Tkinter: libreria per interfaccia grafica. Utile per GUI (graphical user interface)
# fa parte della libreria standarda, non richiede installazioni

import tkinter as tk

# creazione finestra

root = tk.Tk()
root.title("La mia applicazione")   #diamogli un titolo
root.geometry("500x300")            #stabiliamo le dimensioni
root.resizable(False, False)        #per non permettere il resize della finestra
root.configure(bg="orange")     #per colorare lo sfondo
#root.iconbitmap("icona.ico")        #per icona finestra

# Widget sono elementi grafici interattivi come bottoni.
# Hanno struttura gerarchica. Devono essere figli della finestra principale o di un altro widget.

# Label: per inserire testo e immagini non interattive.
etichetta = tk.Label(root, text="Ciao Mondo!") 
etichetta.pack()
# font=("Arial", 16, "bold") per il tipo di carattere
# bg="yellow" per il colore di sfondo
# fg="blue" per il colore del testo
# width=20 per la larghezza in caratteri
# height=2 per l'altezza in linee
# X Immagini: parametro image
# Combinazione testo img: compound

# Button: creazione pulsanti interattivi
pulsante = tk.Button(root, text="Clicca qui")
# Collegare funzioni con: command=funzione (senza parentesi!) con parentesi -> eseguito all'apertura
# Gestire stati con: state="disabled" o state="normal"

# Entry: input testuale
campo = tk.Entry(root)                  #per campi singoli
campo_pwd = tk.Entry(root, show="*")    #per nascondere testo inserito
campo.get()                             #operazioni sui dati
campo.insert(0, "valore")               #impostare valore
campo.delete(0, tk.END)
# per filtrare l'input che l'utente può inserire: validate + la funzione validatecommand

# Text: input testuale lungo
area_testo = tk.Text(root, width=40, height=10) #le dimensioni sono dei caratteri e righe
area_testo.get("1.0", tk.END)

# Avvio: Da tenere alla fine dello script. Il codice dopo non viene eseguito finché la finestra è aperta.
root.mainloop()
print("La finestra è stata chiusa. Arrivederci!")