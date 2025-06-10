# Entry con stile personalizzato
import tkinter as tk

root = tk.Tk()
root.title("Interfaccia Grafica Personalizzata")

entry = tk.Entry(
    root,
    bg="#f0f0f0",
    fg="#333",
    font=("Helvetica", 12),
    bd=2,
    relief="groove",
    highlightthickness=1,
    highlightcolor="red",
)
# Listbox con colori diversi per selezione
listbox = tk.Listbox(
    root,
    bg="yellow",
    fg="red",
    selectbackground="#3366cc",
    selectforeground="white",
    font=("Arial", 10),
)
listbox.insert(tk.END, "Elemento 1")
# Checkbutton personalizzato
check = tk.Checkbutton(
    root,
    text="Opzione",
    activebackground="#e0e0e0",
    font=("Verdana", 11),
    selectcolor="#ccffcc",
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
check.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")


root.mainloop()
