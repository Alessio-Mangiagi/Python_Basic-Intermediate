import tkinter as tk
from PIL import Image, ImageTk
import math

print("><(((º> sabusabu <º)))><")

def show_calcolatrice():
    calcolatrice_frame.pack(fill="both", expand=True)
    tris_frame.pack_forget()

def strumenti():
    print("Strumenti selezionato")

def giochi():
    print("Giochi selezionato")

def applicazioni():
    print("Applicazioni selezionato")

def btn_calcolatrice():
    show_calcolatrice()

root = tk.Tk()
root.title("layaut")
root.geometry("1280x720")
root.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
root.iconbitmap("Studenti\Alessio Mangiagi\icone\favicon.ico")

menu = tk.Menu(
    root,
    bg="#3653D1",
    fg="white",
    activebackground="#4750d2",
    activeforeground="grey",
    font=("Arial", 12)
)
file_menu = tk.Menu(
    menu,
    tearoff=0,
    bg="#3653D1",
    fg="white",
    activebackground="#4750d2",
    activeforeground="#ff0000"
)
file_menu.add_command(label="Apri", command=lambda: print("Apri"))
file_menu.add_command(label="Salva", command=lambda: print("Salva"))
file_menu.add_separator()
file_menu.add_command(label="Esci", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)
root.config(menu=menu)

barra = tk.Frame(root, bg="#292A33")
barra.pack(side="left", fill="y")
barra_bassa = tk.Frame(barra, bg="#292A33")
barra_bassa.pack(side="bottom", fill="y")

main = tk.Frame(root, bg="#3653D1")
main.pack(side="right", fill="both", expand=True)
tk.Label(main, text="Benvenuto in layaut", bg="#3653D1", fg="white", font=("Arial", 24)).pack(pady=20)

# Frame e oggetti per giochi e calcolatrice
tris_frame = tk.Frame(main, bg="#683E68", width=900, height=720)
# tris_game = Tris(tris_frame)  # Decommenta e definisci la classe Tris se necessario

calcolatrice_frame = tk.Frame(main, bg="#222222", width=900, height=720)
# Puoi aggiungere qui il layout della calcolatrice

btn_strumenti = tk.Button(barra, text="Strumenti", bg="#3653D1", fg="white", activebackground="#f7f7f7", activeforeground="grey", width=10, height=2, command=strumenti)
btn_strumenti.pack(pady=10, padx=10, fill="y")
btn_giochi = tk.Button(barra, text="Giochi", bg="#3653D1", fg="white", activebackground="#ffffff", activeforeground="grey", width=10, height=2, command=giochi)
btn_giochi.pack(padx=10, pady=10, fill="y")
btn_applicazioni = tk.Button(barra, text="Applicazioni", bg="#3653D1", fg="white", activebackground="#ffffff", activeforeground="grey", width=10, height=2, command=applicazioni)
btn_applicazioni.pack(padx=10, pady=10, fill="y")
btn_calcolatrice = tk.Button(barra_bassa, text="Calcolatrice", bg="#FFFFFF", fg="black", activebackground="#000000", activeforeground="white", width=10, height=2, command=btn_calcolatrice)
btn_calcolatrice.pack(padx=10, pady=10, fill="y")
btn_note = tk.Button(barra_bassa, text="Note", bg="#FFFFFF", fg="black", activebackground="#000000", activeforeground="white", width=10, height=2, command=lambda: print("Note"))
btn_note.pack(padx=10, pady=10, fill="y")

bottom_menu = tk.Frame(root, bg="#292A33")

root.mainloop()