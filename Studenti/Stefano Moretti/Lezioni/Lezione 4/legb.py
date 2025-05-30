x = "global" # Global scope

def funzione_esterna(): 
    x = "enclosing"
    def funzione_interna():
        x = "local"
        print("Dentro funzione_interna:", x)
    funzione_interna()
    print("Dentro funzione_esterna:", x)

funzione_esterna()
print("Nel modulo globale:", x)