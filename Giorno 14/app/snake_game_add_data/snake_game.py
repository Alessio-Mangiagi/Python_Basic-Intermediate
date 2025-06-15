import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# Costanti per le dimensioni della griglia e della finestra
WIDTH = 500
HEIGHT = 500
GRID_SIZE = 20

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.iconbitmap("app\\resource\\Copilot_20250611_103235.ico")
        
        # Creazione del menu
        self.create_menu()
        
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.setup_game()
        self.bind_controls()
        self.update()
    
    def create_menu(self):
        """Crea la barra dei menu"""
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)
        
        # Menu File
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Nuovo Gioco", command=self.setup_game)
        self.file_menu.add_command(label="Salva Punteggio", command=self.save_score)
        self.file_menu.add_command(label="Carica Punteggio", command=self.load_score)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Esci", command=self.quit_game)
        
        # Menu Opzioni
        self.options_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Opzioni", menu=self.options_menu)
        self.options_menu.add_command(label="Pausa", command=self.toggle_pause)
        
    def setup_game(self):
        """Inizializza il gioco"""
        self.canvas.delete("all")  # Pulisce il canvas
        self.score = 0
        self.snake = [[5, 5]]
        self.food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        self.direction = "Right"
        self.paused = False  # Assicura che il gioco non sia in pausa
        
        self.update_score()
        self.draw_snake()
        self.place_food()
        self.update()  # Riavvia il loop di aggiornamento
    
    def bind_controls(self):
        """Collega i controlli della tastiera"""
        self.master.bind("<KeyPress>", self.on_key_press)
    
    def on_key_press(self, e):
        """Gestisce gli eventi di pressione dei tasti"""
        if e.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = e.keysym
        elif e.keysym == "p":
            self.toggle_pause()
        elif e.keysym == "q":
            self.quit_game()
    
    def toggle_pause(self):
        """Attiva/disattiva la pausa"""
        self.paused = not self.paused
        if self.paused:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="PAUSA", fill="white", font=("Arial", 24))
        else:
            self.canvas.delete("all")
            self.draw_snake()
            self.place_food()
            self.update()
    
    def update(self):
        """Aggiorna lo stato del gioco"""
        if not self.paused:
            self.move_snake()
            self.check_collisions()
            self.canvas.after(100, self.update)
    
    def move_snake(self):
        """Muove il serpente nella direzione attuale"""
        head = self.snake[-1]
        if self.direction == "Up":
            new_head = [head[0], head[1]-1]
        elif self.direction == "Down":
            new_head = [head[0], head[1]+1]
        elif self.direction == "Left":
            new_head = [head[0]-1, head[1]]
        elif self.direction == "Right":
            new_head = [head[0]+1, head[1]]
        
        self.snake.append(new_head)
        if new_head == self.food:
            self.score += 10
            self.update_score()
            self.place_food()
        else:
            self.snake.pop(0)
        
        self.draw_snake()
    
    def draw_snake(self):
        """Disegna il serpente sulla griglia"""
        self.canvas.delete("snake")
        for segment in self.snake:
            x1 = segment[0] * GRID_SIZE
            y1 = segment[1] * GRID_SIZE
            x2 = x1 + GRID_SIZE
            y2 = y1 + GRID_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", tags="snake")
    
    def place_food(self):
        """Posiziona il cibo in una posizione casuale sulla griglia"""
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        self.food = [x, y]
        self.canvas.delete("food")
        x1 = x * GRID_SIZE
        y1 = y * GRID_SIZE
        x2 = x1 + GRID_SIZE
        y2 = y1 + GRID_SIZE
        self.canvas.create_oval(x1, y1, x2, y2, fill="red", tags="food")
    
    def update_score(self):
        """Aggiorna il punteggio sul titolo della finestra"""
        self.master.title(f"Snake Game - Punteggio: {self.score}")
    
    def check_collisions(self):
        """Controlla le collisioni con i bordi e con se stessi"""
        head = self.snake[-1]
        if head in self.snake[:-1] or head[0] < 0 or head[1] < 0 or head[0] >= (WIDTH // GRID_SIZE) or head[1] >= (HEIGHT // GRID_SIZE):
            self.game_over()
    
    def game_over(self):
        """Gestisce la fine del gioco"""
        self.paused = True
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 24))
    
    def save_score(self):
        """Salva il punteggio su file"""
        try:
            with open('snake_score.json', 'w') as f:
                json.dump({'score': self.score}, f)
            messagebox.showinfo("Salvataggio", "Punteggio salvato con successo!")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel salvataggio: {str(e)}")
    
    def load_score(self):
        """Carica il punteggio da file"""
        try:
            if os.path.exists('snake_score.json'):
                with open('snake_score.json', 'r') as f:
                    data = json.load(f)
                    self.score = data['score']
                    messagebox.showinfo("Caricamento", f"Punteggio caricato: {self.score}")
            else:
                messagebox.showinfo("Info", "Nessun punteggio salvato trovato")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel caricamento: {str(e)}")
    
    def quit_game(self):
        """Chiude il gioco"""
        if messagebox.askyesno("Esci", "Vuoi davvero uscire dal gioco?"):
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()