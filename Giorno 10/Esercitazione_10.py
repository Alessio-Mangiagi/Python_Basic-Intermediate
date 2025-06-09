import tkinter as tk  # Importa la libreria per creare interfacce grafiche
import tkinter.messagebox as messagebox  # Importa i messaggi pop-up


class Tris:
    def __init__(self, instanzaTkinter):
        # Inizializza il gioco del Tris
        self.instanzaTkinter = instanzaTkinter  # Salva la finestra principale
        self.instanzaTkinter.title("Tris")  # Imposta il titolo della finestra
        self.current_player = "X"  # Il giocatore corrente inizia con "X"
        self.moves = 0  # Conta le mosse fatte

        # Crea una griglia 3x3 di pulsanti
        self.buttons = []
        for row in range(3):  # Per ogni riga (0, 1, 2)
            current_row = []  # Lista temporanea per la riga corrente
            for col in range(3):  # Per ogni colonna (0, 1, 2)
                button = tk.Button(
                    self.instanzaTkinter,  # Genitore del pulsante
                    text="",  # Testo vuoto inizialmente
                    font=("Helvetica", 32),  # Font grande per vedere bene X e O
                    width=3,  # Larghezza del pulsante
                    height=1,  # Altezza del pulsante
                    # LAMBDA SPIEGAZIONE: lambda crea una funzione "al volo"
                    # r=row, c=col cattura i valori ATTUALI di row e col
                    # Senza questo, tutti i pulsanti chiamerebbero button_click(2,2)
                    # perché row e col sarebbero sempre gli ultimi valori del ciclo
                    command=lambda r=row, c=col: self.button_click(r, c),
                )
                button.grid(row=row, column=col, sticky="nsew")  # Posiziona il pulsante
                current_row.append(button)  # Aggiunge il pulsante alla riga
            self.buttons.append(current_row)  # Aggiunge la riga completa alla griglia

        # Crea il pulsante Reset
        self.reset_button = tk.Button(
            self.instanzaTkinter,
            text="Reset",
            font=("Helvetica", 16),
            command=self.reset_board,  # Chiama reset_board quando premuto
        )
        # Posiziona il pulsante reset sotto la griglia (riga 3)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def button_click(self, row, col):
        """Gestisce il click su un pulsante della griglia"""
        btn = self.buttons[row][col]  # Ottiene il pulsante cliccato
        if btn["text"]:  # Se il pulsante ha già del testo
            return  # Esce dalla funzione (cella già occupata)

        btn.config(text=self.current_player)  # Mette X o O nel pulsante
        self.moves += 1  # Incrementa il contatore delle mosse

        if self.check_winner():  # Controlla se qualcuno ha vinto
            messagebox.showinfo(
                "Vincitore", f"Il giocatore {self.current_player} ha vinto!"
            )
            self.disable_buttons()  # Disabilita tutti i pulsanti
        elif self.moves == 9:  # Se tutte le 9 celle sono piene
            messagebox.showinfo("Pareggio", "La partita è finita in pareggio!")
            self.disable_buttons()
        else:
            # Cambia giocatore: se era X diventa O, se era O diventa X
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

    def check_winner(self):
        """Controlla se c'è un vincitore"""
        container_lines = []  # Lista che conterrà tutte le linee da controllare
        lines = []  # Lista temporanea per costruire ogni linea

        # Controlla le righe orizzontali
        for row in range(3):
            for col in range(3):
                lines.append(
                    self.buttons[row][col]
                )  # Aggiunge ogni pulsante della riga
            container_lines.append(lines)  # Aggiunge la riga completa
            lines = []  # Resetta per la prossima riga

        # Controlla le colonne verticali
        for col in range(3):
            for row in range(3):
                lines.append(
                    self.buttons[row][col]
                )  # Aggiunge ogni pulsante della colonna
            container_lines.append(lines)
            lines = []

        # Controlla la diagonale principale (da alto-sinistra a basso-destra)
        for i in range(3):
            lines.append(self.buttons[i][i])  # [0,0], [1,1], [2,2]
        container_lines.append(lines)
        lines = []

        # Controlla la diagonale secondaria (da alto-destra a basso-sinistra)
        for i in range(3):
            lines.append(self.buttons[i][2 - i])  # [0,2], [1,1], [2,0]
        container_lines.append(lines)

        # Controlla ogni linea per vedere se c'è un vincitore
        for line in container_lines:
            symbols = []  # Lista dei simboli in questa linea
            for btn in line:
                symbols.append(btn["text"])  # Aggiunge il testo di ogni pulsante

            # Se tutti e 3 i simboli sono uguali al giocatore corrente
            if symbols == [self.current_player] * 3:
                # Colora di verde la linea vincente
                for btn in line:
                    btn.config(bg="green")
                return True  # Ha vinto!
        return False  # Nessun vincitore

    def disable_buttons(self):
        """Disabilita tutti i pulsanti quando il gioco finisce"""
        for row in self.buttons:  # Per ogni riga
            for btn in row:  # Per ogni pulsante nella riga
                btn.config(state=tk.DISABLED)  # Disabilita il pulsante

    def reset_board(self):
        """Resetta il gioco per una nuova partita"""
        for row in self.buttons:
            for btn in row:
                btn.config(
                    text="",  # Rimuove il testo
                    bg="SystemButtonFace",  # Ripristina il colore originale
                    state=tk.NORMAL,  # Riabilita il pulsante
                )
        self.current_player = "X"  # Ricomincia con X
        self.moves = 0  # Resetta il contatore mosse


# Crea la finestra principale
root = tk.Tk()
# Crea il gioco passando la finestra
tris_game = Tris(root)
# Avvia il loop principale che mantiene la finestra aperta
root.mainloop()
