class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def __str__(self):
        return f"{self.nome}, {self.età} anni"

persona = Persona("Alice", 30)
print(persona)  # Output: Alice, 30 anni


if __name__ == "__main__":
    # Esempio di utilizzo
    p = Persona("Bob", 25)
    print(p)  # Output: Bob, 25 anni 

