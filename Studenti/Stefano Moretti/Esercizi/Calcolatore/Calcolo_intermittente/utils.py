def check_ore_digiuno(ore_digiuno):
    """
    Controlla se le ore di digiuno sono valide.
    
    Args:
        ore_digiuno (int): Ore di digiuno da controllare.
        
    Returns:
        bool: True se le ore sono valide, False altrimenti.
    """
    if ore_digiuno < 0 or ore_digiuno > 24:
        print("Per favore, inserisci un numero tra 0 e 24.")
        return True
    return False

def esci_programma(x, y):
    """
    Chiede all'utente se vuole continuare o uscire dal programma.
    
    Returns:
        bool: True se l'utente vuole continuare, False altrimenti.
    """
    while y:
        exit = input("Vuoi ancora usare il programma? (S/N) ").lower().strip()
        if exit == 'n':
            print("Alla prossima!")
            y = False
            x = False
            return x
        elif exit == 's':
            x = True
            y = False
            return x
        else:
            print("Per favore, inserisci 'S' o 'N'.")
            continue