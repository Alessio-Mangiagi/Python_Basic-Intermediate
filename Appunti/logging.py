import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='presentazione.log',
    filemode='a'
)

def presentazione():
    """
    Chiede all'utente di inserire il proprio nome e lo saluta.
    Utilizza logging per registrare il nome inserito.
    """
    nome = input("Inserisci il tuo nome: ")
    print("Ciao", nome)
    logging.info(f"Nome inserito: {nome}")
    
presentazione()