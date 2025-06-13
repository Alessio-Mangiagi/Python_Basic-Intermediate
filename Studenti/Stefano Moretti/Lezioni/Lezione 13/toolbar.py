import tkinter as tk

class MenuTendina:
    def __init__(self):

        # Inizializza la finestra principale
        self.root = tk.Tk()
        self.root.title("Prova menu toolbar con sottomenu")
        self.root.geometry("300x150")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Crea il menu File
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)

        # Aggiungi comandi al menu File
        filemenu.add_command(label="Apri")
        
        # Aggiungi un sottomenu per "Apri come"
        filesubmenu = tk.Menu(filemenu, tearoff=0)
        aprisubmenu = tk.Menu(filesubmenu, tearoff=0)
        aprisubmenu.add_command(label="PDF", command=lambda: print("Apri PDF cliccato"))
        aprisubmenu.add_command(label="PNG", command=lambda: print("Apri PNG cliccato"))
        aprisubmenu.add_command(label="DOCX", command=lambda: print("Apri DOCX cliccato"))
        filemenu.add_cascade(label="Apri come", menu=aprisubmenu)

        # Aggiungi un comando per "Salva" e shortcut Ctrl+S
        filemenu.add_command(label="Salva", command=lambda: print("Salva cliccato"), accelerator="Ctrl+S")
        self.root.bind("<Control-s>", lambda event: print("File salvato con Ctrl+S"))

        # Aggiungi un sottomenu per "Salva come"
        salvasubmenu = tk.Menu(filemenu, tearoff=0)
        salvasubmenu.add_command(label="XLS", command=lambda: print("Salva come XLS cliccato"))
        salvasubmenu.add_command(label="PDF", command=lambda: print("Salva come PDF cliccato"))
        salvasubmenu.add_command(label="CSV", command=lambda: print("Salva come CSV cliccato"))
        filemenu.add_cascade(label="Salva come", menu=salvasubmenu)

        # Aggiungi un separatore e commando per uscire
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.root.quit, accelerator="Alt+F4")

        # Crea il menu Esporta
        esportamenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Esporta", menu=esportamenu)
        # Aggiungi un sottomenu per esportare come immagine
        esportasubmenu = tk.Menu(esportamenu, tearoff=0)
        esportasubmenu.add_command(label="PNG", command=lambda: print("Esporta come PNG cliccato"))
        esportasubmenu.add_command(label="JPEG", command=lambda: print("Esporta come JPEG cliccato"))
        esportamenu.add_cascade(label="Esporta come immagine", menu=esportasubmenu)
        # Aggiungi un comando per esportare come PDF
        esportamenu.add_command(label="Esporta come PDF", command=lambda: print("Esporta come PDF cliccato"))

        aiutomenu = tk.Menu(menubar, tearoff=0)
        aiutomenu.add_command(label="Guida", command=lambda: print("Vai su wikipedia"))
        menubar.add_cascade(label="Aiuto", menu=aiutomenu)
        

        



        label = tk.Label(self.root, text="Prova menu toolbar con sottomenu")
        label.pack(pady=40)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MenuTendina()
    app.run()

