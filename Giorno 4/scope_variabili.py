# Esempio per capire la regola LEGB (Local, Enclosing, Global, Built-in)

x = "global"

def funzione_esterna():
    x = "enclosing"
    def funzione_interna():
        x = "local"
        print("Local:", x)  # Cerca x nello scope locale
    funzione_interna()
    print("Enclosing:", x)  # Cerca x nello scope della funzione esterna

def funzione_senza_local():
    print("Global:", x)  # Non trova x localmente, va a cercare nello scope globale

def funzione_built_in():
    print("Built-in:", len([1,2,3]))  # Usa la funzione built-in len

funzione_esterna()
funzione_senza_local()
funzione_built_in()

# Output atteso:
# Local: local
# Enclosing: enclosing
# Global: global
# Built-in: 3
