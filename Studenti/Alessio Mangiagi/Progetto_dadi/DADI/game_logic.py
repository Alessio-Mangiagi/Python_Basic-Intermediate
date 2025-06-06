import random
from . import toolbox_AM
import datetime
import sys
import os
from .variabili_dadi import nomi_giocatori
from .. import test
 
#gioco lancio dadi
while True:
    nome = input("Inserisci il nome del giocatore (o 'fine' per terminare): ")
    if nome.lower() == 'fine':
        break
    nomi_giocatori.append(nome)
x= True
print(selezione := "Seleziona il tipo di dado da lanciare:")
while x:
    print("1. Dado 6","2. Dado 9","3. Dado 12","4. Dado 20","5. Esci", sep="\n")
    
    scelta = input("Inserisci il numero del dado da lanciare: ")
    
    lista_dadi = []
    numero_lanci_dadi = int(input("Quanti dadi vuoi lanciare? "))
    if numero_lanci_dadi <= 0:
        print("Il numero di lanci deve essere maggiore di zero.")
        sys.exit(1)

    if scelta == "1":
        def lancio_dadi():
            dado = random.randint(1, 6)
            lista_dadi.append(dado)
            return dado
    elif scelta == "2":
        def lancio_dadi():
            dado = random.randint(1, 9)
            lista_dadi.append(dado)
            return dado
    elif scelta == "3":
        def lancio_dadi():
            dado = random.randint(1, 12)
            lista_dadi.append(dado)
            return dado
    elif scelta == "4":
        def lancio_dadi():
            dado = random.randint(1, 20)
            lista_dadi.append(dado)
            return dado

    for nome in nomi_giocatori:
            print(f"Giocatore: {nome}")

    for i in range(1, numero_lanci_dadi + 1):
        risultato = lancio_dadi()
        print(f"lancio {i}: {risultato}")
        print(f"Lista dei lanci: {lista_dadi}")
        print(toolbox_AM.Somma_lista(lista_dadi))
        print(f"Il giocatore {nomi_giocatori[0]} ha vinto con un punteggio di {toolbox_AM.Somma_lista(lista_dadi)}!")
end = input("Premi un tasto per uscire.")   
