# TO DO: 
# 1. Creare interfaccia grafica 
# 2 . Aggiungi fame/felicità + vita/salute nella classe Animali.
# -> fame e felicità scendono in base al tempo ed in base alle interazioni.
# Alcuni animali hanno bisogno di più attenzioni? felicità o fame cala più velocemente
# ======================
#           /)/)_
#  ( Hi! > (..   )o
# ======================

import tkinter as tk
from animal_pack.species import Cane, Gatto, Pesce, Pappagallo
from animal_pack.messages import MSG

class AnimalApp(tk.Tk):
    """Main application class for the Little Animals game."""
    def __init__ (self):
        super().__init__()
        self.background = "lightgreen"
        self.configure(bg= self.background)
        self.title("Little Animals")
        self.geometry("900x650")
        self.iconbitmap("images/icon.ico")
        self.language = "it" # Default language
        self.animal = None
        self.starting_frame()
        self.choose_language()

    def starting_frame(self):
        """Initial interface with start, about and exit buttons."""
        self.start_frame = tk.Frame(self, bg="lightgreen")
        self.start_frame.pack(side=tk.TOP, fill=tk.X, pady=20)

        self.logo = tk.PhotoImage(file="images/littleanimals.png")

        # Display logo of the game
        logo_label = tk.Label(self.start_frame, image = self.logo,  bg="lightgreen")
        logo_label.pack()

        button_frame = tk.Frame(self.start_frame, background="lightgreen")
        button_frame.pack(anchor=tk.CENTER, pady= 50)

        start_button = tk.Button(button_frame, text="Start", font=("bold", 30), command= self.start_game)
        start_button.pack(pady=10, side=tk.LEFT, padx=20)

        about_button = tk.Button(button_frame, text="About", font=("bold", 30), command= self.show_about)
        about_button.pack(pady=10, side=tk.LEFT, padx=20)

        exit_button = tk.Button(button_frame, text="Exit", font=("bold", 30), command= quit)
        exit_button.pack(pady=10, side=tk.LEFT, padx=20)

    def set_language(self):
        """Set the selected language."""
        self.language = self.language_var.get()
        self.update_texts()

    def update_texts(self):
        # Aggiorna la label della lingua
        self.lang_label.config(text=MSG[self.language]["set_lang"])

    def choose_language(self):
        """Choose the language for the application with a button."""
        self.lang_frame = tk.Frame(self.start_frame, bg="lightgreen")
        self.lang_frame.pack(side=tk.BOTTOM)

        self.lang_label = tk.Label(self.lang_frame, text= MSG[self.language]["set_lang"], bg="lightgreen")
        self.lang_label.pack(side=tk.LEFT)
        self.language_var = tk.StringVar(value=self.language)

        tk.Radiobutton(
            self.lang_frame, text="Italiano", variable=self.language_var, value="it",
            bg="lightgreen", command=self.set_language).pack(side=tk.LEFT)

        tk.Radiobutton(
            self.lang_frame, text="English", variable=self.language_var, value="eng",
            bg="lightgreen", command=self.set_language).pack(side=tk.LEFT)

    def show_about(self):
        """Show the about message in the selected language."""
        about_msg = MSG[self.language]["about"]

        # adding a frame for about message
        about_frame = tk.Frame(self.start_frame, bg="lightgreen")
        about_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tk.Label(about_frame, text= about_msg, bg="lightgreen", font=("Arial", 14)).pack(pady=10)

        # Making the about frame refresh if you click the button again
        if hasattr(self, 'about_frame'):
            self.about_frame.pack_forget()
            self.about_frame = None
        self.about_frame = about_frame
    
    def start_game(self):
        """Start the game by opening a new frame to choose an animal."""
        self.start_frame.pack_forget()
        self.animal_sel_frame = tk.Frame(self, bg="lightgreen")
        self.animal_sel_frame.pack(fill="both", expand=True)
        
        tk.Label(self.animal_sel_frame, text=MSG[self.language]["sel_animal"], bg="lightgreen", font=("Verdana", 20)).pack(pady=20)



# Avvio dell'applicazione
if __name__ == "__main__":
    app = AnimalApp()
    app.mainloop()