import logging

logging.basicConfig(level=logging.INFO)

"""
Questo script contiene esempi di funzioni Python di base:
- Una funzione per salutare l'utente in base al nome inserito.
- Una funzione che prende due numeri in input e restituisce la somma, la moltiplicazione e la divisione.
Le funzioni sono commentate per scopi didattici.
"""

'''print("hello world")
#funzione salutami
def salutami(name):
    """
    Saluta l'utente in modo personalizzato in base al nome fornito.

    Args:
        name (str): Il nome dell'utente.

    Returns:
        None
    """
    x = "hello \n"
    y = name
    if name == "peppino":
        print("Ciao dev, come stai?")
    elif name == "alessio":
        print("Ciao Padrone, come stai?")
    else: 
        print("Ciao, come stai?")
    frase= x+y
    print(frase)

name = input("Inserisci il tuo nome: ")

salutami(name)'''

#definizione che prende due numeri e restituisce la somma, la moltiplicazione e la divisione
'''def mate():
    """
    Chiede all'utente di inserire due numeri e restituisce una stringa con la somma,
    la moltiplicazione e la divisione dei due numeri.

    Returns:
        str: Risultato delle operazioni matematiche.
    """
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))
    somma = a + b
    moltiplicazione = a * b
    dividisione = a / b
    risultato = f"La somma è: {somma}, la moltiplicazione è: {moltiplicazione}, la divisione è: {dividisione}"
    logging.info("il risultato è stato registrato")
    return risultato
print(mate())
#si può usare per definire più funzioni e avere il risultato'''
