# Importa il modulo tkinter per creare l'interfaccia grafica
import tkinter as tk

# Riga vuota per separazione

# Dizionario che contiene i tipi di carburante con i rispettivi costi per litro in euro
FUEL_TYPES = {"Benzina": 1.5, "Diesel": 1.3, "GPL": 0.8, "Metano": 0.9}

# Riga vuota per separazione


# Funzione di validazione che controlla se l'input è composto solo da cifre
def only_digits(valore):
    """Controlla se il valore inserito è un numero."""
    # Ritorna True se il valore contiene solo cifre o è una stringa vuota
    return valore.isdigit() or valore == ""


# Riga vuota per separazione

# Crea la finestra principale dell'applicazione
root = tk.Tk()
# Imposta il titolo della finestra
root.title("Calcolatore di carburante")
# Registra la funzione di validazione per poterla usare nei widget Entry
vcmd = root.register(only_digits)

# Crea e posiziona l'etichetta per la distanza
label_km = tk.Label(root, text="Distanza percorsa (km):")
label_km.grid(row=0, column=0, padx=10, pady=10)
# Crea il campo di input per i chilometri con validazione
entry_km = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry_km.grid(row=1, column=0, padx=10, pady=10)

# Crea l'etichetta per il tipo di carburante
label_carburante = tk.Label(root, text="Tipo di carburante:")
# Crea una variabile StringVar per gestire la selezione del radio button (valore predefinito: "Benzina")
radio_var = tk.StringVar(value="Benzina")
# Crea il primo radio button per la Benzina
radio_1 = tk.Radiobutton(root, text="Benzina", variable=radio_var, value="Benzina")
radio_1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
# Crea il secondo radio button per il Diesel
radio_2 = tk.Radiobutton(root, text="Diesel", variable=radio_var, value="Diesel")
radio_2.grid(row=3, column=0, padx=10, pady=5, sticky="w")
# Crea il terzo radio button per il GPL
radio_3 = tk.Radiobutton(root, text="GPL", variable=radio_var, value="GPL")
radio_3.grid(row=4, column=0, padx=10, pady=5, sticky="w")
# Crea il quarto radio button per il Metano
radio_4 = tk.Radiobutton(root, text="Metano", variable=radio_var, value="Metano")
radio_4.grid(row=5, column=0, padx=10, pady=5, sticky="w")

# Crea una variabile IntVar per gestire lo stato del checkbox
road_trip = tk.IntVar()
# Crea il checkbox per indicare se è un viaggio su strada
check_road_trip = tk.Checkbutton(root, text="Viaggio su strada", variable=road_trip)
check_road_trip.grid(row=6, column=0, padx=10, pady=5, sticky="w")

# Crea una variabile StringVar per mostrare il risultato del calcolo
result_var = tk.StringVar(value="Costo carburante: --")

# Riga vuota per separazione


# Definisce la funzione per calcolare il costo del carburante
def calcola_costo():
    """Calcola il costo del carburante in base alla distanza e al tipo di carburante."""
    try:
        # Converte l'input dei chilometri in float
        km = float(entry_km.get())
        # Ottiene il tipo di carburante selezionato
        tipo_carburante = radio_var.get()
        # Recupera il costo per litro dal dizionario
        costo_per_litro = FUEL_TYPES[tipo_carburante]
        # Imposta il consumo medio in litri per chilometro
        consumo = 0.1  # Consumo medio in litri per km
        # Calcola il costo totale: chilometri × consumo × costo per litro
        costo_totale = km * consumo * costo_per_litro
        # Se è selezionato "viaggio su strada", aumenta il costo del 20%
        if road_trip.get():
            costo_totale *= 1.2  # Aggiungi un 20% per il viaggio su strada
        # Aggiorna il testo del risultato con il costo formattato a 2 decimali
        result_var.set(f"Costo carburante: {costo_totale:.2f} €")
    # Gestisce l'errore se l'input non è un numero valido
    except ValueError:
        result_var.set("Errore: Inserisci un numero valido.")


# Riga vuota per separazione

# Crea il pulsante per eseguire il calcolo
button_calcola = tk.Button(root, text="Calcola Costo", command=calcola_costo)
button_calcola.grid(row=7, column=0, padx=10, pady=10)
# Crea l'etichetta per mostrare il risultato
label_result = tk.Label(root, textvariable=result_var)
label_result.grid(row=8, column=0, padx=10, pady=10)

# Avvia il loop principale dell'interfaccia grafica
root.mainloop()
