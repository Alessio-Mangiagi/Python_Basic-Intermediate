import tkinter as tk

class app_esercitazione(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Esercitazione OOP e tkinter")
        self.geometry("600x600")
        self.inizializza_toolbar()
        self.nome_var = tk.StringVar(value="inserisci nome")
        self.cognome_var = tk.StringVar(value="inserisci cognome")
        self.inizializza_sezione_body()
        self.inizializza_sezione_testo()
        
        

        

    def inizializza_toolbar(self):
        self.toolbar = tk.Frame(self, bg="lightgray", bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.button_clear = tk.Button(self.toolbar, text="C", command=self.clear())
        self.button_clear.pack(side=tk.LEFT, padx=2, pady=2)

        self.button_info = tk.Button(self.toolbar, text="Info", command=self.show_info())
        self.button_info.pack(side=tk.LEFT, padx=2, pady=2)
        
    def inizializza_sezione_body(self):
        self.sezione_body = tk.Frame(self)
        self.sezione_body.pack(fill=tk.BOTH, expand=True)

        self.label_nome = tk.Label(self.sezione_body, text="Nome:", font=("Arial", 14))
        self.label_nome.pack(pady=10, padx=10, anchor=tk.W)

        self.entry_nome = tk.Entry(self.sezione_body, font=("Arial", 14), textvariable=self.nome_var)
        self.entry_nome.pack(pady=10, padx=10, fill=tk.X)

        self.label_cognome = tk.Label(self.sezione_body, text="Cognome:", font=("Arial", 14))
        self.label_cognome.pack(pady=10, padx=10, anchor=tk.W)

        self.entry_cognome = tk.Entry(self.sezione_body, font=("Arial", 14), textvariable=self.cognome_var)
        self.entry_cognome.pack(pady=10, padx=10, fill=tk.X)

        self.inizializza_sezione_radiobutton()


    def inizializza_sezione_radiobutton(self):
        self.sezione_button = tk.Frame(self.sezione_body, bg="lightgray")
        self.sezione_button.pack(padx=10, pady=10, side=tk.TOP, anchor=tk.CENTER)
        self.radio_genere = tk.StringVar()
        self.radio_genere.set("Maschio")

        self.radio_maschio = tk.Radiobutton(self.sezione_button, text="Maschio", variable=self.radio_genere, value="Maschio")
        """self.radio_maschio.pack(row=0, column=0, padx=5, pady=5, sticky="EW")"""
        self.radio_maschio.pack(side="left", padx=40, pady=5, anchor=tk.CENTER)

        self.radio_femmina = tk.Radiobutton(self.sezione_button, text="Femmina", variable=self.radio_genere, value="Femmina")
        """self.radio_femmina.grid(row=0, column=1, padx=5, pady=5, sticky="EW")"""
        self.radio_femmina.pack(side="left", padx=40, pady=5, anchor=tk.CENTER)

        self.radio_altro = tk.Radiobutton(self.sezione_button, text="Altro", variable=self.radio_genere, value="Altro")
        """self.radio_altro.grid(row=0, column=2, padx=5, pady=5, sticky="EW")"""
        self.radio_altro.pack(side="left", padx=40, pady=5, anchor=tk.CENTER)


    def inizializza_sezione_testo(self):
        self.sezione_testo = tk.Frame(self.sezione_body, bg="lightblue")
        self.sezione_testo.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
        
        self.test_1 = tk.Text(self.sezione_testo, font=("Arial", 14), bg="#e20a0a", height=10, width=50)
        
        self.scrollbar = tk.Scrollbar(self.sezione_testo, command=self.test_1.yview)
        
        self.test_1.config(yscrollcommand=self.scrollbar.set)
        self.test_1.grid(column=0, row=1)
        
        self.scrollbar.grid(column=1, row=1, sticky="ns")
    

    def clear(self):
        print("Clear")

    def show_info(self):
        print("Info: Questa è una calcolatrice con Listbox integrata.")
    

app = app_esercitazione()

app.mainloop()

    