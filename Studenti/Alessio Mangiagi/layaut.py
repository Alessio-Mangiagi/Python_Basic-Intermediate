import tkinter as tk
from PIL import Image, ImageTk

print("><(((º> sabusabu <º)))><")

root = tk.Tk()
root.title("layaut")
root.geometry("1280x720")
root.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
root.iconbitmap("C:\\Users\\Alessio Mangiagi\\Desktop\\pythoncorso_riverloop\\Python_Basic-Intermediate\\Studenti\\Alessio Mangiagi\\icone\\favicon.ico")

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
    activeforeground="grey"
)
file_menu.add_command(label="Apri", command=lambda: print("Apri"))
file_menu.add_command(label="Salva", command=lambda: print("Salva"))
file_menu.add_separator()
file_menu.add_command(label="Esci", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)
root.config(menu=menu)

barra= tk.Frame(root, bg="#292A33")
barra.pack(side= "left" , fill="y")
tool_button = tk.Button(barra, text="Strumenti", bg="#3653D1", fg="white", activebackground="#f7f7f7", activeforeground="grey", width=10, height=2)
tool_button.pack(pady=10, padx=10, fill="y")
tool_button = tk.Button(barra, text="Strumenti", bg="#3653D1", fg="white", activebackground="#ffffff", activeforeground="grey", width=10, height=2) 
tool_button.pack(padx=10, pady=10, fill="y")
tool_button = tk.Button(barra, text="Strumenti", bg="#3653D1", fg="white", activebackground="#ffffff", activeforeground="grey",width=10, height=2)
tool_button.pack(padx=10, pady=10, fill="y")

bottom_menu = tk.Frame(root, bg="#292A33")

root.mainloop()
