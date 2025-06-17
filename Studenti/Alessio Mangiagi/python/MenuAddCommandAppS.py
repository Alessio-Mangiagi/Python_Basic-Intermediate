import tkinter as tk
from tkinter import messagebox
print("><(((º> sabusabu <º)))><")
class MenuAddCommandApp:
    """Applicazione di esempio per la creazione di menu in Tkinter"""
    
    def __init__(self):
        """Inizializza l'applicazione e crea l'interfaccia"""
        self.root = tk.Tk()
        self.root.title("Menu add_command")
        self.root.geometry("350x350")
        self.root.iconbitmap("Studenti\\Alessio Mangiagi\\icone\\favicon.ico")
        # Creazione della barra dei menu
        self.create_menu_bar()
        
        # Creazione dei widget
        self.create_widgets()
        
        # Binding degli shortcut
        self.bind_shortcuts()
        
    def create_menu_bar(self):
        """Crea la barra dei menu e i relativi sottomenu"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu File
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Apri", command=self.apri, accelerator="Ctrl+O")
        filemenu.add_command(label="Salva", command=self.salva, accelerator="Ctrl+S")
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.quit_app, accelerator="Alt+F4")
        
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

    def run(self):
        """Avvia il main loop dell'applicazione"""
        self.root.mainloop()


if __name__ == "__main__":
    app = MenuAddCommandApp()
    app.run()