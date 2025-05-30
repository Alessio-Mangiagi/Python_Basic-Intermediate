"""
lezione_1.1.py

Questo script dimostra le migliori pratiche per documentare un file Python.
Include esempi di docstring per il modulo, per le funzioni e commenti inline.
"""

def somma(a, b):
    """
    Calcola la somma di due numeri.

    Args:
        a (int or float): Il primo numero.
        b (int or float): Il secondo numero.

    Returns:
        int or float: La somma di a e b.
    """
    return a + b

def main():
    """
    Funzione principale dello script.
    Esegue un esempio di somma e stampa il risultato.
    """
    # Definisce due numeri di esempio
    numero1 = 5                             
    numero2 = 7

    # Calcola la somma usando la funzione somma
    risultato = somma(numero1, numero2)

    # Stampa il risultato
    print(f"La somma di {numero1} e {numero2} è {risultato}")


main()
