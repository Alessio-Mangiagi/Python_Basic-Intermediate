# - Interfacce grafiche -

### Giorno 9
- **Teoria: Introduzione a Tkinter: finestra principale, loop, widget base**

1. Cos'è Tkinter e perché usarlo
2. Importazione del modulo Tkinter
3. Creazione della finestra principale (`Tk()`)
4. Il ciclo principale (`mainloop()`)
5. Introduzione ai widget in Tkinter
6. Il widget `Label`: visualizzare testo
7. Il widget `Button`: creare pulsanti
8. Il widget `Entry`: input testuale breve
9. Il widget `Text`: input testuale lungo
10. Il widget `Frame`: contenitore per altri widget
11. Il metodo `.pack()` per il layout semplice
12. Concetto di gerarchia tra widget
13. Attributi base: `bg`, `fg`, `font`, `width`, `height`
14. Differenza tra widget e metodi
15. Cenni su interazione con l’utente

- **Pratica: Creazione di una finestra con etichette, pulsanti, campi di testo**

1. Creazione della finestra con `Tk()`
2. Impostazione del titolo con `.title()`
3. Aggiunta di una `Label` con testo
4. Personalizzazione della `Label` con font e colori
5. Inserimento di un `Button` che stampa un messaggio
6. Inserimento di un campo `Entry`
7. Recupero del testo da `Entry` con `.get()`
8. Inserimento di un campo `Text` multilinea
9. Recupero del contenuto da `Text`
10. Gestione del layout con `.pack()`
11. Collegamento di una funzione al `Button`
12. Visualizzazione dinamica di testo cliccando un bottone
13. Inserimento di due `Label` su righe diverse
14. Inserimento di un `Frame` per raggruppare widget
15. Test completo dell’interfaccia di base

---

### Giorno 10
- **Teoria: Layout manager: pack, grid, place**

1. Cos'è un layout manager
2. Perché usare i layout manager in GUI
3. Introduzione al layout `.pack()`
4. Opzioni di `.pack()` – `side`, `fill`, `expand`
5. Introduzione al layout `.grid()`
6. Sistema a righe e colonne con `.grid()`
7. Opzioni di `.grid()` – `row`, `column`, `padx`, `pady`
8. Introduzione al layout `.place()`
9. Coordinate assolute con `.place()`
10. Differenze tra `.pack()`, `.grid()` e `.place()`
11. Vantaggi e svantaggi di ogni sistema
12. Quando combinare layout manager
13. Restrizioni nell’uso combinato (`pack` vs `grid`)
14. Best practice nei layout complessi
15. Approccio modulare con `Frame` e layout dedicati

- **Pratica: Organizzazione di widget in colonne e righe**

1. Creazione di un'interfaccia con `.grid()`
2. Inserimento di etichette su righe distinte
3. Allineamento di input e label nella stessa riga
4. Utilizzo di colonne multiple con `column=0`, `column=1`
5. Inserimento di pulsanti in griglia
6. Utilizzo di `sticky` per l’allineamento
7. Applicazione di `padx` e `pady`
8. Espansione del layout con `columnspan`
9. Inserimento di spazi verticali tra righe
10. Creazione di una griglia con 3 colonne
11. Inserimento di un `Frame` come cella della griglia
12. Layout complesso con sezioni logiche
13. Uso di `.place()` per elementi decorativi
14. Combinazione di `pack` e `grid` con `Frame` separati
15. Testing della responsività del layout

---

### Giorno 11
- **Teoria: Widget avanzati: Entry, Text, Listbox, Checkbutton, Radiobutton**

1. Funzione del widget `Entry`
2. Differenza tra `Entry` e `Text`
3. Parametri utili di `Entry` (show, width)
4. Il widget `Text`: creazione e gestione
5. Il widget `Listbox`: lista di opzioni
6. Aggiunta e rimozione di elementi in `Listbox`
7. Selezione singola e multipla in `Listbox`
8. Il widget `Checkbutton`: opzioni multiple
9. Gestione del valore con `IntVar()`
10. Il widget `Radiobutton`: scelta singola
11. Uso di `StringVar()` per `Radiobutton`
12. Differenze d’uso tra `Checkbutton` e `Radiobutton`
13. Stili grafici applicabili ai nuovi widget
14. Interazioni tra widget avanzati
15. Validazione dell’input con widget

- **Pratica: Sviluppo di un form interattivo con selezioni multiple**

1. Creazione del layout del form
2. Aggiunta di `Entry` per nome e cognome
3. Inserimento di un `Text` per note
4. Creazione di `Radiobutton` per selezione di genere
5. Inserimento di `Checkbutton` per hobby/interessi
6. Collegamento di variabili a `Checkbutton`
7. Collegamento di variabili a `Radiobutton`
8. Aggiunta di una `Listbox` con selezione multipla
9. Recupero delle selezioni dalla `Listbox`
10. Pulsante per salvare i dati
11. Funzione di stampa dei dati inseriti
12. Validazione dei campi obbligatori
13. Pulizia del form con un secondo pulsante
14. Layout ordinato con `grid()`
15. Test completo del form interattivo

---

### Giorno 12

- **Teoria: Eventi e callback: binding e gestione degli eventi utente**

1. Cos’è un evento in un’interfaccia grafica
2. Tipi di eventi in Tkinter
3. Il concetto di callback function
4. Il metodo `bind()` per associare eventi
5. Eventi da tastiera: `<KeyPress>`, `<Return>`
6. Eventi da mouse: `<Button-1>`, `<Double-Button-1>`
7. Eventi di movimento del mouse
8. Passaggio dell’evento alla funzione
9. `event.x`, `event.y`: coordinate del click
10. Uso del `focus` per rilevare eventi
11. Differenze tra `command` e `bind()`
12. Eventi su `Entry` e `Text`
13. Eventi personalizzati o generici
14. Uso di `lambda` per passare parametri
15. Debug di callback complesse

- **Pratica: Programmazione di risposte a click, keypress, selezioni**

1. Rilevazione del click su un pulsante
2. Rilevazione del click in un’area vuota
3. Visualizzazione delle coordinate del click
4. Rilevazione di pressione tasti in `Entry`
5. Aggiunta di logica su invio (`<Return>`)
6. Cambio dinamico di testo con un click
7. Evidenziare un widget al passaggio del mouse
8. Colorare un campo al ricevimento del focus
9. Uso di `lambda` per passare argomenti
10. Aggiornamento di una `Label` con evento
11. Disabilitare un pulsante dopo il click
12. Rilevazione di doppio click su `Listbox`
13. Utilizzo di `event.char` per filtrare tasti
14. Eventi su pulsanti della tastiera (`Shift`, `Ctrl`)
15. Animazione semplice tramite eventi (es. cambia colore)

---

### Giorno 13
- **Teoria: Menu, dialoghi (messagebox), Canvas per disegno**

1. Introduzione ai menu in Tkinter
2. Costruzione di un menu base
3. Menu a tendina e sottomenu
4. Uso del widget `Menu` con `add_command`
5. Separatori nei menu
6. Collegamento di azioni ai menu
7. Dialoghi di sistema: `messagebox`
8. Tipi di messaggi (`showinfo`, `showwarning`, etc.)
9. Uso di `askyesno`, `askquestion`
10. Importazione del modulo `messagebox`
11. Introduzione al widget `Canvas`
12. Disegno di linee, rettangoli, ovali
13. Coordinate nel `Canvas`
14. Eventi di disegno su `Canvas`
15. Interazione dinamica con oggetti grafici

- **Pratica: Realizzazione di un piccolo editor grafico o disegno semplici**

1. Creazione della finestra e area `Canvas`
2. Aggiunta di menu `File`, `Modifica`
3. Collegamento delle voci a funzioni
4. Uso di `messagebox` per avvisi
5. Disegno libero con mouse (traccia linee)
6. Uso di `bind()` su `Canvas`
7. Disegno di forme fisse con pulsanti
8. Cancellazione del `Canvas`
9. Inserimento di colore nel disegno
10. Selezione colore tramite variabile
11. Aggiornamento del disegno in tempo reale
12. Salvataggio del disegno in un file immagine
13. Messaggio di conferma salvataggio
14. Funzione "Nuovo" che resetta il disegno
15. Testing completo dell’editor

---

### Giorno 14
- **Teoria: Confezionamento dell’app: icona, file eseguibile con PyInstaller**

1. Cos’è il packaging di un’app
2. Differenze tra script e applicazione
3. Preparazione del file `.py` finale
4. Struttura del progetto completo
5. Inserimento di un’icona personalizzata
6. Formato dell’icona: `.ico`
7. Creazione dell’icona o conversione da `.png`
8. Introduzione a PyInstaller
9. Installazione di PyInstaller
10. Comando base per creare un `.exe`
11. Opzione `--onefile` e `--noconsole`
12. Gestione delle risorse esterne (icone, immagini)
13. Integrazione di file extra in PyInstaller
14. Debug di errori comuni nel build
15. Distribuzione e testing dell’eseguibile

- **Pratica: Creazione di un eseguibile standalone del progetto GUI**

1. Preparazione del file Python funzionante
2. Creazione di un’icona `.ico`
3. Posizionamento dell’icona nella cartella progetto
4. Comando `pyinstaller --onefile nomefile.py`
5. Verifica creazione cartella `dist/`
6. Aggiunta di `--icon=icona.ico`
7. Uso dell’opzione `--noconsole`
8. Inclusione di file statici nel bundle
9. Test dell’eseguibile generato
10. Distribuzione su altra macchina
11. Gestione delle dipendenze esterne
12. Firma del file per Windows (facoltativo)
13. Creazione di un file `.bat` per lanciare l’app
14. Compressione della cartella finale
15. Invio dell’app ad altri utenti per test