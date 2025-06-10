# Importa la libreria tkinter per creare l'interfaccia grafica
import tkinter as tk


class FuelType:
    """Classe che rappresenta un tipo di carburante con nome e costo per litro"""

    def __init__(self, name, cost_per_liter):
        """
        Inizializza un tipo di carburante
        Args:
            name (str): Nome del carburante (es. "Benzina", "Diesel")
            cost_per_liter (float): Costo per litro in euro
        """
        self.name = name
        self.cost_per_liter = cost_per_liter


class Viaggio:
    """Classe che rappresenta un viaggio con distanza, tipo di carburante e opzioni"""

    def __init__(self, distance, fuel_type, road_trip=False):
        """
        Inizializza un viaggio
        Args:
            distance (float): Distanza in chilometri
            fuel_type (FuelType): Oggetto FuelType che rappresenta il carburante utilizzato
            road_trip (bool): Se True, applica un sovrapprezzo del 20%
        """
        self.distance = distance
        self.fuel_type = fuel_type
        self.road_trip = road_trip

    def calculate_cost(self):
        """
        Calcola il costo totale del viaggio
        Returns:
            float: Costo totale del carburante per il viaggio
        """
        # Calcola il costo base: distanza * costo per litro
        total_cost = self.distance * self.fuel_type.cost_per_liter
        # Se è un viaggio su strada, aggiunge il 20% di sovrapprezzo
        if self.road_trip:
            total_cost *= 1.2
        return total_cost

    def __str__(self):
        """
        Rappresentazione testuale del viaggio
        Returns:
            str: Stringa formattata con dettagli del viaggio e costo
        """
        # Aggiunge "(Viaggio su strada)" se il flag road_trip è True
        road_trip_str = " (Viaggio su strada)" if self.road_trip else ""
        return f"{self.distance} km con {self.fuel_type.name}{road_trip_str}: {self.calculate_cost():.2f} €"


class FuelCalculatorApp(tk.Tk):
    """Classe principale dell'applicazione GUI per il calcolo del carburante"""

    def __init__(self):
        """Inizializza l'interfaccia grafica e i componenti dell'applicazione"""
        # Chiama il costruttore della classe padre (tk.Tk)
        super().__init__()

        # Imposta il titolo della finestra
        self.title("Calcolatore di carburante")

        # Inizializza le variabili tkinter per memorizzare i valori dell'interfaccia
        self.km_var = tk.StringVar()  # Distanza inserita dall'utente
        self.fuel_type_var = tk.StringVar(
            value="Benzina"
        )  # Tipo di carburante selezionato
        self.road_trip_var = tk.IntVar()  # Checkbox per viaggio su strada (0 o 1)
        self.result_var = tk.StringVar(
            value="Costo carburante: --"
        )  # Risultato del calcolo

        # Dizionario che contiene i tipi di carburante disponibili
        self.fuel_types = {
            "Benzina": FuelType("Benzina", 1.5),
            "Diesel": FuelType("Diesel", 1.3),
            "GPL": FuelType("GPL", 0.8),
            "Metano": FuelType("Metano", 0.9),
        }

        # Lista per memorizzare tutti i viaggi calcolati
        self.viaggi = []

        # Registra la funzione di validazione per accettare solo numeri
        vcmd = self.register(self.only_digits)

        # Creazione dell'interfaccia grafica usando il layout grid

        # Etichetta per il campo distanza
        tk.Label(self, text="Distanza percorsa (km):").grid(
            row=0, column=0, padx=10, pady=10
        )

        # Campo di input per la distanza con validazione numerica
        tk.Entry(
            self, textvariable=self.km_var, validate="key", validatecommand=(vcmd, "%P")
        ).grid(row=1, column=0, padx=10, pady=10)

        # Etichetta per la sezione tipo di carburante
        tk.Label(self, text="Tipo di carburante:").grid(
            row=2, column=0, padx=10, pady=5
        )

        # Radio button per selezionare il tipo di carburante
        tk.Radiobutton(
            self, text="Benzina", variable=self.fuel_type_var, value="Benzina"
        ).grid(row=3, column=0, padx=10, pady=5, sticky="w")

        tk.Radiobutton(
            self, text="Diesel", variable=self.fuel_type_var, value="Diesel"
        ).grid(row=4, column=0, padx=10, pady=5, sticky="w")

        tk.Radiobutton(self, text="GPL", variable=self.fuel_type_var, value="GPL").grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )

        tk.Radiobutton(
            self, text="Metano", variable=self.fuel_type_var, value="Metano"
        ).grid(row=6, column=0, padx=10, pady=5, sticky="w")

        # Checkbox per indicare se è un viaggio su strada
        tk.Checkbutton(
            self, text="Viaggio su strada", variable=self.road_trip_var
        ).grid(row=7, column=0, padx=10, pady=5, sticky="w")

        # Pulsante per avviare il calcolo
        tk.Button(self, text="Calcola", command=self.calculate_cost).grid(
            row=8, column=0, padx=10, pady=10
        )

        # Etichetta per mostrare il risultato del calcolo
        tk.Label(self, textvariable=self.result_var).grid(
            row=9, column=0, padx=10, pady=10
        )

        # Listbox per mostrare lo storico di tutti i viaggi calcolati
        self.listbox = tk.Listbox(self, height=10, width=50)
        self.listbox.grid(row=1, column=1, padx=10, pady=10)

    def only_digits(self, valore):
        """
        Funzione di validazione per accettare solo numeri nell'input
        Args:
            valore (str): Valore inserito dall'utente
        Returns:
            bool: True se il valore contiene solo cifre o è vuoto, False altrimenti
        """
        # Ritorna True se il valore contiene solo cifre o è una stringa vuota
        return valore.isdigit() or valore == ""

    def calculate_cost(self):
        """
        Calcola il costo del carburante e aggiorna l'interfaccia con il risultato
        Gestisce anche eventuali errori di input
        """
        try:
            # Ottiene i valori dall'interfaccia
            km = float(self.km_var.get())  # Converte la distanza in float
            fuel_type = (
                self.fuel_type_var.get()
            )  # Ottiene il tipo di carburante selezionato
            cost_per_liter = self.fuel_types[
                fuel_type
            ].cost_per_liter  # Ottiene il costo per litro

            # Calcola il costo totale
            total_cost = km * cost_per_liter

            # Applica il sovrapprezzo del 20% se è un viaggio su strada
            if self.road_trip_var.get():
                total_cost *= 1.2

            # Aggiorna l'etichetta del risultato
            self.result_var.set(f"Costo carburante: {total_cost:.2f} €")

            # Crea un oggetto Viaggio con i dati inseriti
            obj_viaggio = Viaggio(
                km, self.fuel_types[fuel_type], self.road_trip_var.get() == 1
            )

            # Aggiunge il viaggio alla lista
            self.viaggi.append(obj_viaggio)

            # Aggiunge il viaggio alla listbox per mostrarlo nell'interfaccia
            self.listbox.insert(tk.END, str(obj_viaggio))

        except ValueError:
            # Gestisce l'errore se l'input non è un numero valido
            self.result_var.set("Errore: Inserisci un numero valido per i km.")


# Crea un'istanza dell'applicazione
app = FuelCalculatorApp()

# Configura il ridimensionamento della griglia per rendere l'interfaccia responsive
app.grid_rowconfigure(1, weight=1)  # La riga 1 si espande verticalmente
app.grid_columnconfigure(1, weight=1)  # La colonna 1 si espande orizzontalmente

# Avvia il loop principale dell'interfaccia grafica
app.mainloop()
