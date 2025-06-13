# Importa la libreria tkinter per creare l'interfaccia grafica
import tkinter as tk

# Importa random per generare posizioni casuali del cibo
import random

# Parametri di gioco
WIDTH = 400  # Larghezza della finestra di gioco in pixel
HEIGHT = 400  # Altezza della finestra di gioco in pixel
DELAY = 100  # Ritardo in millisecondi tra ogni movimento del serpente
SIZE = 20  # Dimensione in pixel di ogni blocco del serpente e del cibo


class SnakeGame:
    def __init__(self, master):
        # Salva il riferimento alla finestra principale
        self.master = master
        # Imposta il titolo della finestra
        self.master.title("Snake Game Semplice")
        # Crea il canvas (area di disegno) con sfondo nero
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        # Aggiunge il canvas alla finestra
        self.canvas.pack()

        # Inizializza il serpente come lista di coordinate (x, y)
        # Il primo elemento è la testa, gli altri sono il corpo
        self.snake = [(100, 100), (80, 100), (60, 100)]
        # Direzione iniziale del movimento
        self.direction = "Right"
        # Flag per controllare se il gioco è ancora in corso
        self.running = True

        # Genera la prima posizione del cibo
        self.food = self.spawn_food()

        # Associa i tasti freccia ai cambiamenti di direzione
        # lambda _: ignora l'evento e chiama solo la funzione
        self.master.bind("<Up>", lambda _: self.change_direction("Up"))
        self.master.bind("<Down>", lambda _: self.change_direction("Down"))
        self.master.bind("<Left>", lambda _: self.change_direction("Left"))
        self.master.bind("<Right>", lambda _: self.change_direction("Right"))

        # Avvia il ciclo di aggiornamento del gioco
        self.update()

    def spawn_food(self):
        # Continua a generare posizioni finché non trova una valida
        while True:
            # Genera coordinata x casuale allineata alla griglia
            x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
            # Genera coordinata y casuale allineata alla griglia
            y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
            # Controlla che la posizione non sia occupata dal serpente
            if (x, y) not in self.snake:
                # Restituisce la posizione valida
                return (x, y)

    def change_direction(self, new_dir):
        # Dizionario delle direzioni opposte per evitare inversioni
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        # Cambia direzione solo se non è opposta a quella attuale
        if opposites[new_dir] != self.direction:
            self.direction = new_dir

    def move_snake(self):
        # Ottiene le coordinate della testa del serpente
        head_x, head_y = self.snake[0]
        # Calcola la nuova posizione della testa in base alla direzione
        if self.direction == "Up":
            head_y -= SIZE  # Muove verso l'alto
        elif self.direction == "Down":
            head_y += SIZE  # Muove verso il basso
        elif self.direction == "Left":
            head_x -= SIZE  # Muove verso sinistra
        elif self.direction == "Right":
            head_x += SIZE  # Muove verso destra
        # Crea la nuova posizione della testa
        new_head = (head_x, head_y)

        # Controllo delle collisioni
        if (
            head_x < 0  # Muro sinistro
            or head_x >= WIDTH  # Muro destro
            or head_y < 0  # Muro superiore
            or head_y >= HEIGHT  # Muro inferiore
            or new_head in self.snake  # Collisione con se stesso
        ):
            # Ferma il gioco se c'è una collisione
            self.running = False
            return

        # Aggiunge la nuova testa all'inizio del serpente
        self.snake = [new_head] + self.snake

        # Controlla se il serpente ha mangiato il cibo
        if new_head == self.food:
            # Genera nuovo cibo (il serpente cresce automaticamente)
            self.food = self.spawn_food()
        else:
            # Rimuove l'ultimo segmento per mantenere la lunghezza
            self.snake.pop()

    def draw(self):
        # Cancella tutto quello che è stato disegnato prima
        self.canvas.delete("all")
        # Disegna ogni segmento del serpente
        for x, y in self.snake:
            # Crea un rettangolo verde per ogni segmento
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green")
        # Ottiene le coordinate del cibo
        fx, fy = self.food
        # Disegna il cibo come rettangolo rosso
        self.canvas.create_rectangle(fx, fy, fx + SIZE, fy + SIZE, fill="red")
        # Se il gioco è finito, mostra il messaggio
        if not self.running:
            # Crea testo "GAME OVER" al centro dello schermo
            self.canvas.create_text(
                WIDTH // 2,  # Posizione x al centro
                HEIGHT // 2,  # Posizione y al centro
                text="GAME OVER",  # Testo da mostrare
                fill="white",  # Colore del testo
                font=("Arial", 24, "bold"),  # Font, dimensione e stile
            )

    def update(self):
        # Muove il serpente solo se il gioco è ancora in corso
        if self.running:
            self.move_snake()
        # Ridisegna sempre lo schermo
        self.draw()
        # Programma il prossimo aggiornamento solo se il gioco continua
        if self.running:
            # Chiama questa funzione di nuovo dopo DELAY millisecondi
            self.master.after(DELAY, self.update)


# Crea la finestra principale di tkinter
root = tk.Tk()
# Crea un'istanza del gioco passando la finestra
game = SnakeGame(root)
# Avvia il loop principale di tkinter (mantiene la finestra aperta)
root.mainloop()
