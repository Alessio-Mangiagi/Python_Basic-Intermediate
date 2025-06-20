import tkinter as tk
from tkinter import messagebox  

print("><(((º> sabusabu <º)))><")
class nuovo_chat:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nuo")   
        self.root.geometry("900x500")    
        self.root.iconbitmap("Studenti\\Alessio Mangiagi\\icone\\favicon.ico")
        self.create_menu_bar()
        self.create_widgets()
        self.bind_shortcuts()
  
  
    def create_widgets(self):
        """Crea i widget dell'interfaccia"""
        self.label = tk.Label(
            self.root, 
            text="Clicca su Apri o Salva nel menu File",
            font=("Arial", 12)
        )
        self.label.pack(pady=40)
        
    def bind_shortcuts(self):
        """Associa gli shortcut ai comandi"""
        self.root.bind("<Control-o>", lambda e: self.apri())
        self.root.bind("<Control-s>", lambda e: self.salva())
        
    def apri(self):
        """Gestisce il comando Apri"""
        self.label.config(text="Hai cliccato Apri")
        messagebox.showinfo("Apri", "Funzione Apri selezionata")

    def salva(self):
        """Gestisce il comando Salva"""
        self.label.config(text="Hai cliccato Salva")
        messagebox.showinfo("Salva", "Funzione Salva selezionata")
        
    def quit_app(self):
        """Chiude l'applicazione con conferma"""
        if messagebox.askyesno("Esci", "Vuoi davvero uscire?"):
            self.root.quit()            
        def show_info():
            print("Mostra informazioni")
        def show_message():
            message = entry.get()
            if message:
                messagebox.showinfo("Messaggio", message)
            else:
                messagebox.showwarning("Attenzione", "Inserisci un messaggio da visualizzare.")


        toolbar = tk.Frame(self.root, bg="#292A33", bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        bottone_clear = tk.Button(toolbar, text="Pulisci", command=quit, bg="#4750d2", fg="white") 
        bottone_clear.pack(side=tk.LEFT, padx=2, pady=2)
        botton_info = tk.Button(toolbar, text="Mostra Messaggio", command=show_message, bg="#4750d2", fg="white")
        botton_info.pack(side=tk.LEFT, padx=2, pady=2)

        var_nome = tk.StringVar()

        entry = tk.Entry(root, font=("Arial", 14))  
        entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 

if __name__ == "__main__":
    nuovo_chat()
    
    print("><(((º> sabusabu <º)))><")