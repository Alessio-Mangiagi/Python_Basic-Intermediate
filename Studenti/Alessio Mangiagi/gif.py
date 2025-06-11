import tkinter as tk
from itertools import count
from PIL import Image, ImageTk

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
            pass  # fine dei frame

        self.delay = delay
        self.frame_index = 0
        self.update_animation()

    def update_animation(self):
        self.config(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.after(self.delay, self.update_animation)

root = tk.Tk()
anim = AnimatedGIF(root, "C:\\Users\\Alessio Mangiagi\\Desktop\\pythoncorso_riverloop\\Python_Basic-Intermediate\\Studenti\\Alessio Mangiagi\\icone\hololive-gawr-gura.gif", delay=100)
anim.pack()
root.mainloop()

#si riferisce al gioco dei numeri 

import os
import random
# ...existing code...

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
            # Mostra GIF animata random alla vittoria
            import tkinter as tk
            from itertools import count
            from PIL import Image, ImageTk

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

            # Scegli una GIF random dalla cartella
            cartella_gif = "C:\\Users\\Alessio Mangiagi\\Desktop\\pythoncorso_riverloop\\Python_Basic-Intermediate\\Studenti\\Alessio Mangiagi\\icone"
            gif_files = [f for f in os.listdir(cartella_gif) if f.lower().endswith(('.gif'))]
            if gif_files:
                gif_path = os.path.join(cartella_gif, random.choice(gif_files))
                gif = AnimatedGIF(self.master, gif_path, delay=100)
                gif.pack()
# ...existing code...