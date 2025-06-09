import tkinter as tk
import tkinter.messagebox as messagebox


class Tris:
    def __init__(self, instanzaTkinter):
        self.instanzaTkinter = instanzaTkinter
        self.instanzaTkinter.title("Tris")
        self.current_player = "X"
        self.moves = 0

        self.buttons = []
        for row in range(3):
            current_row = []
            for col in range(3):
                button = tk.Button(
                    self.instanzaTkinter,
                    text="",
                    font=("Helvetica", 32),
                    width=3,
                    height=1,
                    command=lambda r=row, c=col: self.button_click(r, c),
                )
                button.grid(row=row, column=col, sticky="nsew")
                current_row.append(button)
            self.buttons.append(current_row)

        self.reset_button = tk.Button(
            self.instanzaTkinter,
            text="Reset",
            font=("Helvetica", 16),
            command=self.reset_board,
        )
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def button_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"]:
            return  # La cella è già occupata
        btn.config(text=self.current_player)
        self.moves += 1
        if self.check_winner():
            messagebox.showinfo(
                "Vincitore", f"Il giocatore {self.current_player} ha vinto!"
            )
            self.disable_buttons()
        elif self.moves == 9:
            messagebox.showinfo("Pareggio", "La partita è finita in pareggio!")
            self.disable_buttons()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        container_lines = []
        lines = []

        for c in range(3):
            for r in range(3):
                lines.append(self.buttons[r][c])
            container_lines.append(lines)
            lines = []

        for i in range(3):
            lines.append(self.buttons[i][i])

        container_lines.append(lines)
        lines = []
        for i in range(3):
            lines.append(self.buttons[i][2 - i])
        container_lines.append(lines)
        lines = []

        for line in container_lines:
            symbols = []
            for btn in line:
                symbols.append(btn["text"])

            if (
                symbols == [self.current_player] * 3
            ):  # Controlla se tutti i simboli sono uguali in 3 per riga
                for btn in line:
                    btn.config(bg="green")
                return True
        return False

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(
                    state=tk.DISABLED
                )  # Disabilita i pulsanti dopo la vittoria o il pareggio

    def reset_board(self):
        for row in self.buttons:
            for btn in row:
                btn.config(text="", bg="SystemButtonFace", state=tk.NORMAL)
        self.current_player = "X"
        self.moves = 0


root = tk.Tk()
tris_game = Tris(root)
root.mainloop()
