import tkinter as tk


class Paint(tk.Tk):
    """Classe principale per l'applicazione Paint che eredita da tk.Tk"""

    def __init__(self):
        """Inizializza l'applicazione Paint"""
        super().__init__()
        self.title("Paint")  # Imposta il titolo della finestra
        self.geometry("600x600")  # Imposta le dimensioni della finestra
        self.last = [0, 0]  # Memorizza l'ultima posizione del mouse per il disegno
        self.line_width = 1  # Spessore della linea di default
        self.line_color = "black"  # Colore della linea di default
        # Inizializza i componenti dell'interfaccia
        self.Initialize_toolbar()
        self.Initialiaze_Body()
        self._bind_events()

    def clear(self):
        """Cancella il contenuto dell'applicazione (da implementare)"""
        print("Clear button clicked")

    def show_info(self):
        """Mostra informazioni sull'applicazione"""
        print("Info: This is a simple Tkinter application.")

    def Enter_Callback(self, event, color="lightblue"):
        """Callback per quando il mouse entra sopra un widget - cambia colore di sfondo"""
        print("Mouse entered widget:", event.widget)
        event.widget.config(bg=color)

    def Leave_Callback(self, event, color="lightgray"):
        """Callback per quando il mouse esce da un widget - ripristina colore originale"""
        print("Mouse left widget:", event.widget)
        event.widget.config(bg=color)

    def start_drawing(self, event):
        """Inizia il disegno memorizzando la posizione iniziale del mouse"""
        self.last = [event.x, event.y]

    def draw(self, event, mode="draw"):
        """Disegna sul canvas quando il mouse viene mosso"""
        x, y = event.x, event.y  # Ottiene le coordinate correnti del mouse
        if self.last != [0, 0]:  # Controlla se esiste una posizione precedente
            if mode == "draw":
                # Modalità disegno: crea una linea con il colore selezionato
                # Disegna una linea dal punto precedente al punto corrente
                self.canvas.create_line(
                    self.last[0],  # Coordinata x del punto precedente
                    self.last[1],  # Coordinata y del punto precedente
                    x,  # Coordinata x del punto corrente
                    y,  # Coordinata y del punto corrente
                    fill=self.line_color,  # Colore della linea selezionato
                    width=self.line_width,  # Spessore della linea selezionato
                    capstyle=tk.ROUND,  # Rende gli estremi delle linee rotondi
                    smooth=True,  # Rende la linea più fluida
                    splinesteps=36,  # Migliora la qualità della curva
                )
            else:
                # Modalità cancellazione: disegna con il colore di sfondo del canvas
                self.canvas.create_line(
                    self.last[0],  # Coordinata x del punto precedente
                    self.last[1],  # Coordinata y del punto precedente
                    x,  # Coordinata x del punto corrente
                    y,  # Coordinata y del punto corrente
                    fill=self.canvas["bg"],  # Usa il colore di sfondo come "gomma"
                    width=self.line_width + 5,  # Gomma più spessa della matita
                    capstyle=tk.ROUND,  # Rende gli estremi delle linee rotondi
                    smooth=True,  # Rende la linea più fluida
                    splinesteps=36,  # Migliora la qualità della curva
                )
        self.last = [x, y]  # Aggiorna la posizione precedente

    def active_drawing(self):
        """Attiva la modalità disegno"""
        self.canvas.bind("<B1-Motion>", lambda e: self.draw(e, "draw"))

    def active_erase(self):
        """Attiva la modalità cancellazione"""
        self.canvas.bind("<B1-Motion>", lambda e: self.draw(e, "erase"))

    def Increase_size(self, event):
        """Aumenta lo spessore della linea di disegno"""
        self.line_width += 1
        print(f"Line width increased to {self.line_width}")

    def Decrease_size(self, event):
        """Diminuisce lo spessore della linea di disegno (minimo 1)"""
        if self.line_width > 1:
            self.line_width -= 1
            print(f"Line width decreased to {self.line_width}")
        else:
            print("Line width cannot be decreased further")

    def set_color(self, color):
        """Imposta il colore per il disegno"""
        self.line_color = color
        print(f"Line color set to {self.line_color}")

    def Initialize_toolbar(self):
        """Inizializza la barra degli strumenti superiore"""
        # Crea il frame della toolbar

        # Crea il menu principale della finestra
        self.toolbarmenu = tk.Menu(self)
        # Configura la finestra per utilizzare il menu creato
        self.config(menu=self.toolbarmenu)

        # Crea un sottomenu "Opzioni" senza la possibilità di essere staccato
        self.optionbar = tk.Menu(self.toolbarmenu, tearoff=0)
        # Aggiunge il sottomenu "Opzioni" al menu principale
        self.toolbarmenu.add_cascade(label="Opzioni", menu=self.optionbar)
        # Crea un ulteriore sottomenu per le informazioni
        self.infobar = tk.Menu(self.optionbar, tearoff=0)
        # Aggiunge un comando "Clear" al menu Opzioni che chiama il metodo clear()
        self.optionbar.add_command(label="Clear", command=self.clear)
        # Aggiunge il sottomenu "Info" al menu "Opzioni"
        self.optionbar.add_cascade(label="Info", menu=self.infobar)
        # Aggiunge un comando "About" al sottomenu Info che chiama show_info()
        self.infobar.add_command(label="About", command=self.show_info)
        # Aggiunge un comando "Help" al sottomenu Info che chiama show_info()
        self.infobar.add_command(label="Help", command=self.show_info)

        # Aggiunge una linea di separazione visiva nel menu Opzioni
        self.optionbar.add_separator()
        # Aggiunge un comando "Exit" che chiude l'applicazione
        self.optionbar.add_command(label="Exit", command=self.quit)

    def Initialize_color_picker(self):
        """Crea una finestra separata per la selezione dei colori"""
        # Finestra popup per i colori
        self.color_frame = tk.Toplevel(self)
        self.color_frame.title("Seleziona Colore")
        self.color_frame.geometry("300x200")

        # Bottoni per i diversi colori
        self.button_red = tk.Button(
            self.color_frame,
            bg="red",
            command=lambda: self.set_color("red"),
        )
        self.button_red.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

        self.button_green = tk.Button(
            self.color_frame,
            bg="green",
            command=lambda: self.set_color("green"),
        )
        self.button_green.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

        self.button_blue = tk.Button(
            self.color_frame,
            bg="blue",
            command=lambda: self.set_color("blue"),
        )
        self.button_blue.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

        self.button_yellow = tk.Button(
            self.color_frame,
            bg="yellow",
            command=lambda: self.set_color("yellow"),
        )
        self.button_yellow.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

        self.button_black = tk.Button(
            self.color_frame,
            bg="black",
            command=lambda: self.set_color("black"),
        )
        self.button_black.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

        # Bottone per chiudere la finestra colori
        self.button_close = tk.Button(
            self.color_frame,
            text="Chiudi",
            command=self.color_frame.destroy,
        )
        self.button_close.pack(padx=2, pady=2, side=tk.TOP, fill=tk.X, expand=True)

    def initialize_tool_disegno(self):
        """Inizializza la barra degli strumenti di disegno laterale"""
        # Frame per gli strumenti di disegno
        self.tool_frame = tk.Frame(self.body_frame, bg="lightgray")
        self.tool_frame.pack(side=tk.LEFT, padx=2, pady=2, anchor="n")

        # Bottone per attivare la matita
        self.button_matita = tk.Button(
            self.tool_frame,
            text="Matita",
            command=self.active_drawing,
        )
        self.button_matita.pack(padx=2, pady=2, side=tk.TOP)

        # Bottone per attivare la gomma
        self.button_gomma = tk.Button(
            self.tool_frame,
            text="Gomma",
            command=self.active_erase,
        )

        # Bottone per aprire il selettore di colori
        self.button_seleziona_colore = tk.Button(
            self.tool_frame,
            text="Seleziona Colore",
            command=self.Initialize_color_picker,
        )
        self.button_seleziona_colore.pack(padx=2, pady=2, side=tk.TOP)

        self.button_gomma.pack(padx=2, pady=2, side=tk.TOP)

    def Initialiaze_Body(self):
        """Crea il corpo principale dell'applicazione"""
        # Frame principale del corpo
        self.body_frame = tk.Frame(self)
        self.body_frame.pack(fill=tk.BOTH, expand=True)

        # Etichetta con istruzioni
        self.label = tk.Label(
            self.body_frame,
            text="Disegna quello che vuoi",
            anchor="center",
            justify=tk.CENTER,
        )
        self.label.pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

        # Inizializza gli strumenti di disegno
        self.initialize_tool_disegno()

        # Canvas principale per il disegno
        self.canvas = tk.Canvas(self.body_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def _bind_events(self):
        """Associa gli eventi ai widget dell'applicazione"""
        # Eventi hover per i bottoni della toolbar

        # Eventi del mouse sul canvas
        self.canvas.bind("<B1-Motion>", self.draw)  # Trascinamento con tasto sinistro
        self.canvas.bind("<Button-1>", self.start_drawing)  # Click tasto sinistro
        self.canvas.bind(
            "<Button-2>", self.Increase_size
        )  # Click tasto centrale (aumenta spessore)
        self.canvas.bind(
            "<Button-3>", self.Decrease_size
        )  # Click tasto destro (diminuisce spessore)


# Crea e avvia l'applicazione
app = Paint()
app.mainloop()
