#indovina il numero
import random
import tkinter as tk
from itertools import count
from PIL import Image, ImageTk
print("><(((º> sabusabu <º)))><")
# Indovina il Numero 

class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        super().__init__(master)
        self.frames = []
        img = Image.open(path)
        try:
            for i in count(1):
                frame = ImageTk.PhotoImage(img.copy())
                self.frames.append(frame)
                img.seek(i)
        except EOFError:
            pass
        self.delay = delay
        self.frame_index = 0
        self.update_animation()

    def update_animation(self):
        self.config(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.after(self.delay, self.update_animation)

class IndovinaNumeroGUI:
    def __init__(self, master):
        self.master = master
        master.title("Indovina il Numero!")
        self.gif = None  # Per gestire la GIF animata
        self.reset_game()

        self.label = tk.Label(master, text="INDOVINA IL NUMERO!!!\nInserisci un numero tra 1 e 99")
        self.label.pack(fill="both")

        self.entry = tk.Entry(master)
        self.entry.pack(fill="both")
        self.button = tk.Button(master, text="Invia", bg="#4750d2", fg="white", command=self.check_number)
        self.button.pack(fill="both")

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(fill="both")

        self.restart_button = tk.Button(master, text="Ricomincia", bg="#4750d2", fg="white", command=self.reset_game)
        self.restart_button.pack(fill="both")
        

    def reset_game(self):
        self.x = random.randint(1, 99)
        self.tentativi = 0
        if hasattr(self, 'result_label'):
            self.result_label.config(text="")
        if hasattr(self, 'entry'):
            self.entry.delete(0, tk.END)
        # Rimuovi la GIF se presente
        if self.gif is not None:
            self.gif.destroy()
            self.gif = None

    def check_number(self):
        try:
            numero = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Inserisci un numero valido!")
            return
        self.tentativi += 1
        if self.x < numero:
            self.result_label.config(text="Troppo! RIPROVA")
        elif self.x > numero:
            self.result_label.config(text="Troppo poco! RIPROVA")
        else:
            self.result_label.config(text=f"{self.x} indovinato in {self.tentativi} tentativi!")
            # Mostra GIF animata alla vittoria
            if self.gif is None:
                self.gif = AnimatedGIF(
                    self.master,
                    "C:\\Users\\Alessio Mangiagi\\Desktop\\pythoncorso_riverloop\\Python_Basic-Intermediate\\Studenti\\Alessio Mangiagi\\icone\\hololive-gawr-gura.gif",
                    delay=100
                )
                self.gif.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = IndovinaNumeroGUI(root)
    root.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
    root.iconbitmap("Studenti\Alessio Mangiagi\icone\favicon.ico")
    # Configura la griglia PRIMA del mainloop
    for i in range(6):  
        root.rowconfigure(i, weight=1)
    for j in range(6):  
        root.columnconfigure(j, weight=1)
    root.mainloop()

print("><(((º> sabusabu <º)))><")
