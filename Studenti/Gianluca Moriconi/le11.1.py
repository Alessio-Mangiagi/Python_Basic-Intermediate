import tkinter as tk

# Programma che visualizza una listbox con alcuni linguaggi di programmazione di esempio
# quando selezioni un elemento, nel Text a destra compare un breve messaggio in console.
# Puoi aggiungere nuovi elementi tramite una casella di testo e un pulsante aggiungi.
# Puoi eliminare l'elemento selezionato con un pulsante apposito.


def on_select(event):
    """Mostra il messaggio del linguaggio selezionato nella console."""
    # Ottiene gli indici degli elementi selezionati nella listbox
    selected_index = listbox.curselection()

    # Itera attraverso tutti gli elementi selezionati
    for i in selected_index:
        # Ottiene il testo dell'elemento selezionato
        selected_item = listbox.get(i)
        # Stampa il messaggio nella console
        print(f"Hai selezionato: {selected_item}")
        # Pulisce l'area di testo (dalla posizione 1.0 alla fine)
        text_area.delete(1.0, tk.END)


def add_item():
    """Aggiunge un nuovo elemento alla Listbox."""
    # Ottiene il testo dalla casella di input e rimuove spazi vuoti
    new_item = entry.get().strip()

    # Controlla se il testo non è vuoto
    if new_item:
        # Aggiunge l'elemento alla fine della listbox
        listbox.insert(tk.END, new_item)
        # Pulisce la casella di testo dopo l'aggiunta
        entry.delete(0, tk.END)


def delete_selected():
    """Elimina l'elemento selezionato dalla Listbox."""
    # Ottiene gli indici degli elementi selezionati
    selected_index = listbox.curselection()

    # Elimina gli elementi selezionati (iterando attraverso gli indici)
    for i in selected_index:
        listbox.delete(i)


# Creazione della finestra principale
root = tk.Tk()
root.title("Esempio Listbox e Text")  # Imposta il titolo della finestra
root.geometry("600x400")  # Imposta le dimensioni della finestra

# Creazione della Listbox con selezione multipla
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 14), width=20)
listbox.pack(side=tk.LEFT, fill=tk.Y)  # Posiziona a sinistra, riempie verticalmente
listbox.bind(
    "<<ListboxSelect>>", on_select
)  # Associa l'evento di selezione alla funzione

# Popola la listbox con linguaggi di programmazione predefiniti
for elemento in [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "Ruby",
    "Go",
    "Rust",
    "Swift",
]:
    listbox.insert(tk.END, elemento)  # Inserisce ogni elemento alla fine della lista

# Creazione della casella di testo per inserire nuovi elementi
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(
    side=tk.TOP, fill=tk.X, padx=10, pady=10
)  # Posiziona in alto, riempie orizzontalmente

# Creazione del pulsante "Aggiungi"
btn = tk.Button(root, text="Aggiungi", font=("Arial", 14), command=add_item)
btn.pack(side=tk.TOP, padx=10, pady=5)  # Posiziona sotto la casella di testo

# Creazione del pulsante "Elimina Selezione"
btn_delete = tk.Button(
    root,
    text="Elimina Selezione",
    font=("Arial", 14),
    command=delete_selected,
)
btn_delete.pack(side=tk.TOP, padx=10, pady=5)  # Posiziona sotto il pulsante aggiungi

# Creazione dell'area di testo a destra
text_area = tk.Text(root, font=("Arial", 14), height=10)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Avvia il loop principale dell'interfaccia grafica
root.mainloop()
