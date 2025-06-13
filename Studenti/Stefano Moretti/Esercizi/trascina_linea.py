import tkinter as tk

class TrascinaLineaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trascina Linea")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, bg="white", width=300, height=200)
        self.canvas.pack(pady=30)
        self.retta = self.canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
        self.selected = None
        self.offset_x = 0
        self.offset_y = 0
        self.canvas.bind("<Button-1>", self.seleziona_linea)
        self.canvas.bind("<B1-Motion>", self.trascina_linea)
        self.canvas.bind("<ButtonRelease-1>", self.deseleziona_linea)

    def seleziona_linea(self, event):
        # Trova la linea più vicina al click
        obj = self.canvas.find_closest(event.x, event.y)[0] 
        self.selected = obj
        # Evidenzia la linea selezionata
        self.canvas.itemconfig(obj, fill="red", width=3)
        # Calcola offset per trascinamento
        coords = self.canvas.coords(obj)
        self.offset_x = event.x - coords[0]
        self.offset_y = event.y - coords[1]

    def trascina_linea(self, event):
        if self.selected:
            coords = self.canvas.coords(self.selected) # Ottiene le coordinate attuali
            new_x1 = event.x - self.offset_x
            new_y1 = event.y - self.offset_y
            new_x2 = new_x1 + (coords[2] - coords[0])
            new_y2 = new_y1 + (coords[3] - coords[1])
            self.canvas.coords(self.selected, new_x1, new_y1, new_x2, new_y2)

    def deseleziona_linea(self, event):
        if self.selected:
            self.canvas.itemconfig(self.selected, fill="blue", width=2)
            self.selected = None # Nessuna linea selezionata


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TrascinaLineaApp()
    app.run()