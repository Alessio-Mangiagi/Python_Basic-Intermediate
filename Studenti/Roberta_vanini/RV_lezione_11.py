import tkinter as tk

# visualizza listbox con alcuni linguaggi di programmazione
# selezionando un elemento viene mostrato un messaggio a destra
# casella di testo per inserire nuovo linguaggio
# puoi eleminare elemento usando un bottone

def on_select(event):
    """Mostra il linguaggio selezionato."""
    selected_language = listbox.get(listbox.curselection())
    message_label.config(text=f"Linguaggio selezionato: {selected_language}")

def add_language():
    """Aggiunge un nuovo linguaggio alla listbox."""
    new_language = entry.get()
    if new_language:
        listbox.insert(tk.END, new_language)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Lista Linguaggi di Programmazione")
root.geometry("600x400")

button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=10, pady=10)

listbox = tk.Listbox(button_frame, width=50, height=20)
listbox.pack(side=tk.TOP, padx=15, pady=10)

message_label = tk.Label(root, text="Seleziona un linguaggio dalla lista", width=50, height=20)
message_label.pack(side=tk.TOP, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

# Aggiunta di alcuni linguaggi di programmazione alla listbox
languages = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "Ruby",
    "PHP",
    "Swift",
    "Go",
    "Rust",
    "Kotlin"
]

for language in languages:
    listbox.insert(tk.END, language)
    
# Casella di testo per inserire un nuovo linguaggio
entry = tk.Entry(button_frame, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Bottone per aggiungere il nuovo linguaggio
add_button = tk.Button(button_frame, text="Aggiungi Linguaggio", command=add_language)
add_button.pack(side=tk.LEFT, padx=10, pady=10)

# Bottone per eliminare il linguaggio selezionato
def delete_language():
    """Elimina il linguaggio selezionato dalla listbox."""
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

delete_button = tk.Button(button_frame, text="Elimina Linguaggio", command=delete_language)
delete_button.pack(side=tk.LEFT, padx=0, pady=10)

# Avvio del main loop dell'applicazione
root.mainloop()