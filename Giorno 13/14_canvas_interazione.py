import tkinter as tk

class CanvasInterazioneApp:
    def __init__(self):
        self.root = tk.Tk()  # Crea la finestra principale
        self.root.title("Canvas Interazione Oggetti")  # Imposta il titolo della finestra
        self.root.geometry("400x300")  # Imposta la dimensione della finestra
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)  # Crea il widget Canvas
        self.canvas.pack(pady=30)  # Posiziona il Canvas nella finestra
        self.rect = self.canvas.create_rectangle(50, 50, 150, 120, fill="orange")  # Disegna un rettangolo
        self.oval = self.canvas.create_oval(180, 80, 260, 150, fill="skyblue")  # Disegna un ovale
        self.selected = None  # ID dell'oggetto selezionato
        self.offset_x = 0  # Offset X per il trascinamento
        self.offset_y = 0  # Offset Y per il trascinamento
        self.canvas.bind("<Button-1>", self.seleziona_oggetto)  # Associa il click sinistro alla selezione
        self.canvas.bind("<B1-Motion>", self.trascina_oggetto)  # Associa il trascinamento col tasto sinistro
        self.canvas.bind("<ButtonRelease-1>", self.deseleziona_oggetto)  # Associa il rilascio del tasto alla deselezione

    def seleziona_oggetto(self, event):
        # Trova l'oggetto più vicino al click
        obj = self.canvas.find_closest(event.x, event.y)[0]  # Restituisce l'ID dell'oggetto più vicino
        self.selected = obj  # Salva l'ID dell'oggetto selezionato
        # Evidenzia l'oggetto selezionato
        self.canvas.itemconfig(obj, outline="red", width=3)  # Cambia il bordo dell'oggetto selezionato
        # Calcola offset per trascinamento
        coords = self.canvas.coords(obj)  # Ottiene le coordinate dell'oggetto
        self.offset_x = event.x - coords[0]  # Calcola la differenza X tra click e oggetto
        self.offset_y = event.y - coords[1]  # Calcola la differenza Y tra click e oggetto

    def trascina_oggetto(self, event):
        if self.selected:
            coords = self.canvas.coords(self.selected)  # Ottiene le coordinate attuali
            w = coords[2] - coords[0]  # Calcola la larghezza
            h = coords[3] - coords[1]  # Calcola l'altezza
            new_x1 = event.x - self.offset_x  # Nuova coordinata X1
            new_y1 = event.y - self.offset_y  # Nuova coordinata Y1
            new_x2 = new_x1 + w  # Nuova coordinata X2
            new_y2 = new_y1 + h  # Nuova coordinata Y2
            self.canvas.coords(self.selected, new_x1, new_y1, new_x2, new_y2)  # Aggiorna le coordinate dell'oggetto

    def deseleziona_oggetto(self, event):
        if self.selected:
            # Ripristina outline
            self.canvas.itemconfig(self.selected, outline="black", width=1)  # Ripristina il bordo originale
            self.selected = None  # Nessun oggetto selezionato

    def run(self):
        self.root.mainloop()  # Avvia il ciclo principale dell'applicazione

if __name__ == "__main__":
    app = CanvasInterazioneApp()
    app.run()
