import tkinter as tk

# L’esercizio prevede una mini-app che permette di inserire il proprio nome, cliccare un bottone oppure premere Invio per mostrare un saluto,
# e passare il mouse sopra la label per cambiarne il colore.


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Esercitazione 12")
        self.geometry("800x600")

        self.label_nome = tk.Label(self, text="Inserisci il tuo nome:")
        self.label_nome.pack(pady=10)
        self.button_counter = 0
        self.color_counter = 0

        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=10)

        self.button_saluto = tk.Button(self, text="Saluto", command=self.mostra_saluto)
        self.button_saluto.pack(pady=10)
        self.entry_nome.bind("<Return>", lambda e: self.mostra_saluto())

        self.checkbox_saluto = tk.BooleanVar()

        self.checkbox = tk.Checkbutton(
            self,
            text="Mostra saluto formale",
            variable=self.checkbox_saluto,
        )
        self.checkbox.pack(pady=10)

        self.radiobutton_saluti = tk.StringVar(value="blue")
        self.radiobutton_rosso = tk.Radiobutton(
            self, text="rosso", variable=self.radiobutton_saluti, value="red"
        )
        self.radiobutton_rosso.pack(pady=5)
        self.radiobutton_verde = tk.Radiobutton(
            self, text="verde", variable=self.radiobutton_saluti, value="green"
        )
        self.radiobutton_verde.pack(pady=5)
        self.radiobutton_blu = tk.Radiobutton(
            self, text="blu", variable=self.radiobutton_saluti, value="blue"
        )
        self.radiobutton_blu.pack(pady=5)
        self.label_counter_button = tk.Label(self, text = "Button counter: " + str(self.button_counter))
        self.label_color_counter = tk.Label(self, text = "Color counter: " + str(self.color_counter))
        self.label_counter_button.pack(pady=10)
        self.label_color_counter.pack(pady=10)


    def mostra_saluto(self):
        self.button_counter += 1
        self.label_counter_button.config( text = "Counter button: " + str(self.button_counter) )
        nome = self.entry_nome.get()
        if self.checkbox_saluto.get():
            self.label_saluto = tk.Label(self, text=f"Ciao {nome}!")
        else:
            self.label_saluto = tk.Label(self, text=f"Non ti saluto {nome}!")
        self.label_saluto.pack(pady=10)
        self.label_saluto.bind(
            "<Enter>", lambda e: self.cambia_colore(e, self.radiobutton_saluti.get())
        )
        self.label_saluto.bind("<Leave>", self.cambia_colore)

    def cambia_colore(self, event, colore="black"):
        self.label_saluto.config(fg=colore)
        self.color_counter +=1
        self.label_color_counter.config( text = "Color counter: " + str(self.color_counter))



instanza_app = App()
instanza_app.mainloop()
