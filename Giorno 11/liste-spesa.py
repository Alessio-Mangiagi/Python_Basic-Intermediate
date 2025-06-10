import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- dati di esempio ---------------------------------------
# Una lista di tuple (nome, prezzo) che rappresenta gli articoli della spesa
items = [
    ("Pane", 1.50),
    ("Latte", 0.90),
    ("Uova", 2.10),
    ("Pasta", 0.80),
]


# -------------------- callback ----------------------------------------------
def update_sum(event=None):
    """Aggiorna la selezione dei prezzi e il totale."""
    # Ottiene gli indici degli elementi selezionati nella listbox degli alimenti
    idxs = listbox_food.curselection()

    # Se nessun elemento è selezionato, resetta tutto
    if not idxs:
        listbox_price.selection_clear(0, tk.END)  # Deseleziona tutti i prezzi
        total_var.set("Totale: 0.00 €")  # Resetta il totale
        return

    # Sincronizza la selezione nella listbox dei prezzi con quella degli alimenti
    listbox_price.selection_clear(0, tk.END)  # Prima deseleziona tutto
    for i in idxs:
        listbox_price.selection_set(i)  # Poi seleziona gli stessi indici

    # Calcola il totale sommando i prezzi degli elementi selezionati
    totale = sum(items[i][1] for i in idxs)
    total_var.set(f"Totale: {totale:.2f} €")  # Aggiorna l'etichetta del totale


def add_item():
    """Aggiunge un nuovo alimento + prezzo alle due Listbox."""
    # Ottiene il nome dell'articolo dall'entry, rimuovendo spazi iniziali/finali
    nome = entry_name.get().strip()

    # Tenta di convertire il prezzo in float, gestendo sia virgola che punto decimale
    try:
        prezzo = float(entry_price.get().replace(",", "."))
    except ValueError:
        # Mostra errore se il prezzo non è un numero valido
        messagebox.showerror("Errore", "Inserisci un prezzo numerico (es. 1.20).")
        return

    # Verifica che il nome non sia vuoto
    if not nome:
        messagebox.showwarning("Attenzione", "Il nome non può essere vuoto.")
        return

    # Aggiunge il nuovo articolo alla lista dati
    items.append((nome, prezzo))
    # Aggiunge il nome alla listbox degli alimenti
    listbox_food.insert(tk.END, nome)
    # Aggiunge il prezzo formattato alla listbox dei prezzi
    listbox_price.insert(tk.END, f"{prezzo:.2f} €")

    # Pulisce i campi di input dopo l'aggiunta
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)


# -------------------- UI ----------------------------------------------------
# Crea la finestra principale
root = tk.Tk()
root.title("Lista della Spesa con Totale")

# Frame principale con padding per spaziatura
main = ttk.Frame(root, padding=10)
main.pack(fill="both", expand=True)

# --- intestazioni -----------------------------------------------------------
# Frame per le intestazioni delle colonne
header = ttk.Frame(main)
header.pack(fill="x")
# Etichetta per la colonna "Alimenti"
ttk.Label(header, text="Alimenti", width=20, anchor="center").pack(side="left")
# Etichetta per la colonna "Prezzo"
ttk.Label(header, text="Prezzo", width=10, anchor="center").pack(side="right")

# --- Listbox affiancate -----------------------------------------------------
# Frame contenitore per le due listbox
list_frame = ttk.Frame(main)
list_frame.pack(fill="both", expand=True)

# Listbox per gli alimenti con selezione multipla estesa
listbox_food = tk.Listbox(
    list_frame, selectmode="extended", height=10, exportselection=False
)
listbox_food.pack(side="left", fill="both", expand=True)
# Collega l'evento di selezione alla funzione update_sum
listbox_food.bind("<<ListboxSelect>>", update_sum)

# Listbox per i prezzi (solo visualizzazione)
listbox_price = tk.Listbox(list_frame, height=10)
listbox_price.pack(side="right", fill="both")

# Carica gli elementi iniziali nelle listbox
for nome, prezzo in items:
    listbox_food.insert(tk.END, nome)  # Aggiunge il nome
    listbox_price.insert(tk.END, f"{prezzo:.2f} €")  # Aggiunge il prezzo formattato

# --- area "aggiungi nuovo" --------------------------------------------------
# Frame per i controlli di aggiunta nuovo articolo
add_frame = ttk.Frame(main, padding=(0, 8))
add_frame.pack(fill="x")

# Campo di input per il nome dell'articolo
entry_name = ttk.Entry(add_frame, width=18)
entry_name.pack(side="left", padx=(0, 4))
entry_name.insert(0, "Nuovo articolo")  # Testo placeholder

# Campo di input per il prezzo
entry_price = ttk.Entry(add_frame, width=8)
entry_price.pack(side="left", padx=(0, 4))
entry_price.insert(0, "0.00")  # Valore placeholder


# Registra il validatore per il campo prezzo
def validate_price(char):
    """Valida che il carattere inserito sia valido per un prezzo (cifre, punto, virgola)."""
    return char.isdigit() or char in ".,\b"


# Registra la funzione di validazione
validate_price_cmd = root.register(validate_price)

# Applica il validatore al campo prezzo
entry_price.config(validate="key", validatecommand=(validate_price_cmd, "%S"))

# Pulsante per aggiungere l'articolo
ttk.Button(add_frame, text="Aggiungi", command=add_item).pack(side="left")

# --- etichetta totale -------------------------------------------------------
# Variabile per il testo del totale
total_var = tk.StringVar(value="Totale: 0.00 €")
# Etichetta che mostra il totale con font più grande e grassetto
ttk.Label(main, textvariable=total_var, font=("Helvetica", 14, "bold")).pack(
    pady=(8, 0)
)

# Avvia il loop principale dell'interfaccia grafica
root.mainloop()
