import tkinter as tk

root = tk.Tk()
root.title("Demo di .place()")
root.geometry("300x200")  # larghezza x altezza in pixel

# Widget posizionato con coordinate assolute
btn_assoluto = tk.Button(root, text="Assoluto\n(x=20, y=30)")
btn_assoluto.place(x=20, y=30)  # 20 px da sinistra, 30 px dall’alto

# Widget posizionato con coordinate relative
btn_relativo = tk.Button(root, text="Relativo\n(relx=0.5, rely=0.5)")
btn_relativo.place(
    relx=0.5, rely=0.5, anchor="center"  # 50 % della larghezza e altezza finestra
)  # ancorato sul centro (default sarebbe NW)

# Widget che si ridimensiona in modo proporzionale
label_resize = tk.Label(root, text="Cresce con la finestra", bg="lightblue")
label_resize.place(
    relx=0.1,
    rely=0.8,  # in basso
    relwidth=0.8,  # 80 % della larghezza finestra
    relheight=0.15,
)  # 15 % dell’altezza finestra

root.mainloop()
