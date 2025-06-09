import tkinter as tk

root = tk.Tk()  
root.title("app")   
root.geometry("900x700")
root.configure(bg="#313131")    


menu = tk.Frame(root, bg="darkgrey", width=200, height=700)
menu.pack(side="left", fill="y")


main_frame = tk.Frame(menu, bg="#00000", width=200, height=200) 
menu.pack(side="right", fill="both", expand=True)
benvenuto = tk.Label(main_frame, text="benvenuto",background="darkgrey", width=300, heigth=200)


sotto = tk.Frame(menu, bg="#f1f1f1", width=200 , height=200 )
sotto.pack(side="bottom", fill="x") 


calcolatrice_button = tk.Button(menu, text="Calcolatrice", bg="orange", fg="white", font="arial")
calcolatrice_button.pack(pady=10)

tris_button = tk.Button(menu, text="Tris", bg="orange", fg="white", font="arial")
tris_button.pack(pady=10)



tetris_button = tk.Button(menu, text="Giochi", bg="orange", fg="white", font="arial")
tetris_button.pack(pady=10)

settings_button = tk.Button(sotto, text="Settings", bg="orange", fg="white", font="arial")
settings_button.pack(pady=10)


root.mainloop()
