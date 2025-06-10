import tkinter as tk

# applicazione con menu su sx con più funzoni (giochi, tools e settings)

root = tk.Tk()
root.title("La mia applicazione")
root.geometry("1200x800")
root.configure(bg="#3c3c3c")

menu = tk.Frame(root, bg="#404040", width=200, height=750)
menu.pack(side="left", fill="y")

bottom_menu = tk.Frame(menu, bg="#341C1C", height=150)
bottom_menu.pack(side="bottom", fill="x")

main_frame = tk.Frame(root, bg="#3c3c3c", width=900, height=720)
main_frame.pack(side="right", fill="both", expand=True)
tk.Label(main_frame, text="Benvenuto nella mia applicazione!", bg="#3c3c3c", fg="#FFFFFF", font=("Helvetica", 24)).pack(pady=20)

sotto = tk.Frame(root, bg="#231F28", width=1000, height=750)
sotto.pack(side="right", fill="x")

calcolatrice_button = tk.Button(menu, text="Calcolatrice", bg="#404040", fg="#FFFFFF", font=("Helvetica", 16), width=20)
calcolatrice_button.pack(pady=10)

tris_button = tk.Button(menu, text="Giochi", bg="#404040", fg="#FFFFFF", font=("Helvetica", 16), width=20)
tris_button.pack(pady=10)

tools_button = tk.Button(menu, text="Tools", bg="#404040", fg="#FFFFFF", font=("Helvetica", 16), width=20)
tools_button.pack(pady=10)

settings_button = tk.Button(menu, text="Settings", bg="#404040", fg="#FFFFFF", font=("Helvetica", 16), width=20)
settings_button.pack(pady=10)

root.mainloop()