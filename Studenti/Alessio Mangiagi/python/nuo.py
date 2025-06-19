import tkinter as tk
from tkinter import messagebox  

root = tk.Tk()
root.title("Nuo")   
root.geometry("900x500")    

def clear():
    entry.delete(0, tk.END)
    
def show_info():
    print("Mostra informazioni")
def show_message():
    message = entry.get()
    if message:
        messagebox.showinfo("Messaggio", message)
    else:
        messagebox.showwarning("Attenzione", "Inserisci un messaggio da visualizzare.")


toolbar = tk.Frame(root, bg="#292A33", bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)
bottone_clear = tk.Button(toolbar, text="Pulisci", command=clear, bg="#4750d2", fg="white") 
bottone_clear.pack(side=tk.LEFT, padx=2, pady=2)
botton_info = tk.Button(toolbar, text="Mostra Messaggio", command=show_message, bg="#4750d2", fg="white")
botton_info.pack(side=tk.LEFT, padx=2, pady=2)

var_nome = tk.StringVar()

entry = tk.Entry(root, font=("Arial", 14))  
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 

root.mainloop()