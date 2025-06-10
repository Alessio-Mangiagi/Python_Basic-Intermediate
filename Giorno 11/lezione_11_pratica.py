import tkinter as tk

root = tk.Tk()
root.title("Calcolatrice con Listbox")
root.geometry("600x600")


def clear():
    print("Clear")


def show_info():
    print("Info: Questa è una calcolatrice con Listbox integrata.")


# Sezione  toolbar
toolbar = tk.Frame(root, bg="lightgray", bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)
button_clear = tk.Button(toolbar, text="C", command=lambda: clear())
button_clear.pack(side=tk.LEFT, padx=2, pady=2)
button_info = tk.Button(toolbar, text="Info", command=lambda: show_info())
button_info.pack(side=tk.LEFT, padx=2, pady=2)

sezione_body = tk.Frame(root)
sezione_body.pack(fill=tk.BOTH, expand=True)

var = tk.StringVar()

label_nome = tk.Label(sezione_body, text="Nome:", font=("Arial", 14))
label_nome.pack(pady=10, padx=10, anchor=tk.W)

entry_nome = tk.Entry(sezione_body, font=("Arial", 14))
entry_nome.pack(pady=10, padx=10, fill=tk.X)

label_cognome = tk.Label(sezione_body, text="Cognome:", font=("Arial", 14))
label_cognome.pack(pady=10, padx=10, anchor=tk.W)
entry_cognome = tk.Entry(sezione_body, font=("Arial", 14))
entry_cognome.pack(pady=10, padx=10, fill=tk.X)


root.mainloop()
