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

nome_var = tk.StringVar(value="Mario")

cognome_var = tk.StringVar(value="Rossi")


label_nome = tk.Label(sezione_body, text="Nome:", font=("Arial", 14))
label_nome.pack(pady=10, padx=10, anchor=tk.W)

entry_nome = tk.Entry(sezione_body, font=("Arial", 14), textvariable=nome_var)
entry_nome.pack(pady=10, padx=10, fill=tk.X)

label_cognome = tk.Label(sezione_body, text="Cognome:", font=("Arial", 14))
label_cognome.pack(pady=10, padx=10, anchor=tk.W)
entry_cognome = tk.Entry(sezione_body, font=("Arial", 14), textvariable=cognome_var)
entry_cognome.pack(pady=10, padx=10, fill=tk.X)

#sezione listbox
sezione_testo = tk.Frame(sezione_body, bg="lightblue")
sezione_testo.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
# text
test_1 = tk.Text(sezione_testo, font=("Arial", 14), bg="#e20a0a", height=10, width=50)
scrollbar = tk.Scrollbar(sezione_testo, command=test_1.yview,)
test_1.config(yscrollcommand=scrollbar.set)
test_1.grid(column=0, row=1) 
scrollbar.grid(column=1 , row=1, sticky="ns")


root.mainloop()
