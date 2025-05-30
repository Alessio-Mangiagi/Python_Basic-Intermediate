class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def __str__(self):
        return f"{self.nome}, {self.età} anni"
    
persona =Persona("Alice", 30)
print(persona) # Output: Alice, 30 anni

if __name__ == "main"
_
persona = Persona("Alice", 30)
print(persona)  # Output: Bob, 30 anni