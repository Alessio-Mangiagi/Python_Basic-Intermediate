class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"'{self.titolo}' di {self.autore}"


libro = Libro("Il Piccolo Principe", "Saint-Exupéry")

print(libro)  # 'Il Piccolo Principe' di Saint-Exupéry
