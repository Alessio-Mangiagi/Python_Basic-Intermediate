import tkinter as tk

root = tk.Tk()
root.title("Finestra Tkinter con Sfondo Rosso")
root.configure(bg="red")

btn = tk.Button(root, text="Cliccami")
btn.pack(pady=20)

root.mainloop()

# Se il file si chiama "tkinter.py", va in conflitto con il modulo standard "tkinter".
# Rinomina questo file, ad esempio in "tkinter_test.py", per evitare l'errore di importazione.
