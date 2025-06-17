import tkinter as tk  # Importa la libreria per creare interfacce grafiche
import tkinter.messagebox as messagebox  # Importa i messaggi pop-up
from openai import OpenAI  # Importa la libreria OpenAI per l'IA
import os
from dotenv import load_dotenv  # Importa per caricare le variabili d'ambiente
import random  # Importa per generare mosse casuali

load_dotenv()  # Carica le variabili d'ambiente dal file .env

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


class TrisAI:
    def __init__(self, instanzaTkinter):
        # Inizializza il gioco del Tris
        self.instanzaTkinter = instanzaTkinter  # Salva la finestra principale
        self.instanzaTkinter.title(
            "Tris Gioca Contro l' AI"
        )  # Imposta il titolo della finestra

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
                    command=lambda r=row, c=col: self.on_human_click(r, c),
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

    def on_human_click(self, row, col):
        """Gestisce il click su un pulsante da parte dell'umano"""
        btn = self.buttons[row][col]
        if btn["text"]:
            return
        btn.config(text="X")
        self.moves += 1
        if self.check_winner():
            messagebox.showinfo("Vincitore", "Il giocatore X ha vinto!")
            self.disable_buttons()
            return
        if self.moves == 9:
            messagebox.showinfo("Pareggio", "La partita è finita in pareggio!")
            self.disable_buttons()
            return
        self.ai_move()  # Chiede all'IA di fare la sua mossa

    def ai_move(self):
        self.current_player = "O"  # L'IA gioca come O

        board = []  # Crea una rappresentazione della griglia
        for row in self.buttons:
            board_row = []
            for btn in row:
                if btn["text"] == "X":
                    board_row.append("X")
                elif btn["text"] == "O":
                    board_row.append("O")
                else:
                    board_row.append("")
            board.append(board_row)
        row, col = self._ask_openai_for_move(
            board
        )  # Chiede all'IA di calcolare la mossa
        self.buttons[row][col].config(text="O")
        self.moves += 1  # Incrementa il contatore delle mosse
        if self.check_winner():
            messagebox.showinfo("Vincitore", "GPT (O) ha vinto!")
            self.disable_buttons()
        self.current_player = "X"  # Cambia di nuovo il turno all'umano

    def _ask_openai_for_move(self, board):
        """Chiede all'IA di calcolare la mossa migliore"""
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Tic Tac Toe player. Suggest the best move for O. and answer directly with 'row,col'.",
                    },
                    {
                        "role": "user",
                        "content": f"Given the board state {board}, suggest a move for O in the format 'row,col'.",
                    },
                ],
            )
            move = response.choices[0].message.content.strip()
            row, col = map(int, move.split(","))  # Converte la risposta in due numeri
            return row, col  # Ritorna la riga e colonna suggerite
        except Exception as e:
            print(f"Errore durante la richiesta all'IA: {e}")
            pass
        empties = [
            (r, c) for r in range(3) for c in range(3) if not self.buttons[r][c]["text"]
        ]
        return random.choice(
            empties
        )  # Se c'è un errore, sceglie una cella vuota a caso

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
tris_game = TrisAI(root)
# Avvia il loop principale che mantiene la finestra aperta
root.mainloop()
