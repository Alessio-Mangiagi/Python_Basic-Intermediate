import tkinter as tk

# applicazione con menu su sx con più funzioni (giochi, tools e settings)
# parte destra l'applicativo

# creazione finestra
root = tk.Tk()
root.title("La mia applicazione")   #diamogli un titolo
root.geometry("1200x720")            #stabiliamo le dimensioni
root.configure(bg="#3C3535")

# creazione del frame a sinestra
menu = tk.Frame(root, bg="#000000", width=300, height=720)
menu.pack(side="left", fill="y")

bottom_menu = tk.Frame(menu, bg="#000000", width=300, height=150)
bottom_menu.pack(side="bottom", fill="x")

# crazione bottoni 
calcolatrice_button = tk.Button(menu, text="Calcolatrice", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
calcolatrice_button.pack(pady=10)

tris_button = tk.Button(menu, text="Tris", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
tris_button.pack(pady=10)

tools_button = tk.Button(menu, text="Tools", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
tools_button.pack(pady=10)

settings_button = tk.Button(bottom_menu, text="Settings", bg="#404040", fg="#FFFFFF", font=("Arial", 16), width=20)
settings_button.pack(pady=10)

root.mainloop() # per avvio, da mettere alla fine del codice