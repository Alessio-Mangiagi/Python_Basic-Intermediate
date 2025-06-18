# Importazioni necessarie
import tkinter as tk
from tkinter import messagebox
import random

# Costanti di gioco
WIDTH = 400
HEIGHT = 400
DELAY = 100
SIZE = 20

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.root = tk.Tk()
        self.root.title("Menu con separatore")
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Nuovo")
        filemenu.add_command(label="Apri")
        filemenu.add_separator()
        filemenu.add_command(label="Esci", command=self.quit)
        self.root.geometry("350x150")
        label = tk.Label(self.root, text="Menu con separatore tra Apri ed Esci")
        label.pack(pady=40)
        self.setup_game()
        self.bind_controls()
        self.update()
        
    def run(self):
        self.root.mainloop()
        
    def quit(self):
        self.root.quit()
        
    def setup_game(self):
        """Inizializza le variabili di gioco"""
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.running = True
        self.score = 0
        self.food = self.spawn_food()
    
    def bind_controls(self):
        """Associa i tasti ai comandi"""
        self.master.bind("<Up>", lambda _: self.change_direction("Up"))
        self.master.bind("<Down>", lambda _: self.change_direction("Down"))
        self.master.bind("<Left>", lambda _: self.change_direction("Left"))
        self.master.bind("<Right>", lambda _: self.change_direction("Right"))
        self.master.bind("<space>", lambda _: self.toggle_pause())

    def toggle_pause(self):
        """Gestisce la pausa del gioco"""
        self.running = not self.running
        if self.running:
            self.update()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
            y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_dir):
        opposites = {
            "Up": "Down", 
            "Down": "Up", 
            "Left": "Right", 
            "Right": "Left"
        }
        if opposites[new_dir] != self.direction:
            self.direction = new_dir

    def move_snake(self):
        head_x, head_y = self.snake[0]
        
        # Calcola nuova posizione
        if self.direction == "Up": head_y -= SIZE
        elif self.direction == "Down": head_y += SIZE
        elif self.direction == "Left": head_x -= SIZE
        elif self.direction == "Right": head_x += SIZE
        
        # Gestione attraversamento bordi
        head_x = head_x % WIDTH
        head_y = head_y % HEIGHT
        new_head = (head_x, head_y)

        # Controllo collisioni con se stesso
        if new_head in self.snake[1:]:
            self.game_over()
            return

        self.snake.insert(0, new_head)
        
        # Gestione cibo
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def game_over(self):
        """Gestisce la fine del gioco"""
        self.running = False
        if messagebox.askyesno("Game Over", f"Punteggio: {self.score}\nVuoi ricominciare?"):
            self.setup_game()

    def draw(self):
        self.canvas.delete("all")
        
        # Disegna serpente
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green2")
        
        # Disegna cibo
        food_x, food_y = self.food
        self.canvas.create_rectangle(
            food_x, food_y, 
            food_x + SIZE, food_y + SIZE, 
            fill="red"
        )
        
        # Mostra punteggio
        self.canvas.create_text(
            50, 20, 
            text=f"Score: {self.score}",
            fill="white",
            font=("Arial", 12)
        )
        
        if not self.running:
            self.canvas.create_text(
                WIDTH//2, HEIGHT//2,
                text="GAME OVER",
                fill="white",
                font=("Arial", 24, "bold")
            )

    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.master.after(DELAY, self.update)
        else:
            self.draw()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
