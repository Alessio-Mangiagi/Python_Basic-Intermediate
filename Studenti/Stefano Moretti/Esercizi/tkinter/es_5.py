import tkinter as tk


FUEL_TYPES ={"Benzina": 1.5, "Diesel": 1.2, "GPL": 0.8, "Metano": 0.9}


def only_digits(valore):
    return valore.isdigit()
    """
    Returns True if the string s contains only digits, False otherwise.
    """
root = tk.Tk()
root.title("Lista della Spesa")
vcmd =root.register(only_digits)

label_km = tk.Label(root, text="Distanza percorsa (km):")
label_km.grid(row=0, column=0, padx=10, pady=10)
entry_km = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'))
entry_km.grid(row=1, column=0, padx=10, pady=10)

label_carburante = tk.Label(root, text="Tipo di carburante:")
radio_var = tk.StringVar(value="Benzina")
radio_1 = tk.Radiobutton(root, text="Benzina", variable=radio_var, value="Benzina")
radio_1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
radio_2= tk.Radiobutton(root, text="Diesel", variable=radio_var, value="Diesel")
radio_2.grid(row=3, column=0, padx=10, pady=5, sticky="w")
radio_3 = tk.Radiobutton(root, text="GPL", variable=radio_var, value="GPL")
radio_3.grid(row=4, column=0, padx=10, pady=5, sticky="w")  
radio_4 = tk.Radiobutton(root, text="Metano", variable=radio_var, value="Metano")
radio_4.grid(row=5, column=0, padx=10, pady=5, sticky="w")

road_trip= tk.IntVar()
check_road_trip = tk.Checkbutton(root, text="Viaggio su strada", variable=road_trip)
check_road_trip.grid(row=6, column=0, padx=10, pady=5, sticky="w")

result_var = tk.StringVar(value="Costo carburante: --")

def calculate_cost():
    try:
        km = float(entry_km.get())
        tipo_carburante = radio_var.get()
        costo_per_litro = FUEL_TYPES[tipo_carburante]
        consumo = 0.1  # Assumiamo un consumo di 10 litri ogni 100 km
        costo_totale = km * consumo * costo_per_litro 
        if road_trip.get():
            costo_totale *= 1.2
        result_var.set(f"Costo carburante: {costo_totale:.2f} €")
    except ValueError:
        result_var.set("Errore: Inserisci un numero valido.")

button_calcola = tk.Button(root, text="Calcola Costo", command=calculate_cost)
button_calcola.grid(row=7, column=0, padx=10, pady=10)
label_result = tk.Label(root, textvariable=result_var)
label_result.grid(row=8, column=0, padx=10, pady=10)
root.mainloop()


