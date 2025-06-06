# TO DO: 
# 1. Inserire traduzioni in inglese:
#       - Fare nuovo file "messages"
#       - Creare dizionario contenente dizionari "IT" e "ENG" dove scrivere le versioni dei testi 
#       - Creare key con alias le linee di testo (uguali per IT ed ENG) e associarle al testo nella lingua specifica 
# 2 . Aggiungi fame/felicità + vita/salute nella classe Animali.
# -> fame e felicità scendono in base al tempo ed in base alle interazioni.
# Alcuni animali hanno bisogno di più attenzioni? felicità o fame cala più velocemente
# ======================
#           /)/)_
#  ( Hi! > (..   )o
# ======================

from animal_pack.species import Cane, Gatto, Pesce, Pappagallo
from animal_pack.messages import MSG

# ===========================
# Funzione di Interazione
# ===========================

def scegli_lingua():
    while True:
        lingua = input("Seleziona la lingua / Select language (it/en): ").lower()
        if lingua in MSG:
            return lingua
        print("Lingua non supportata / Language not supported.")

def il_mio_animale():
    lingua = scegli_lingua()
    msg = MSG[lingua]
    nome = input(msg["nome"])

    while True: # selezione della specie
        specie = input(msg["specie"]).lower()

        animale = None
        if specie == ("cane" if lingua == "it" else "dog"):
            animale = Cane(nome, lingua)
        elif specie == ("gatto" if lingua == "it" else "cat"):
            animale = Gatto(nome, lingua)
        elif specie == ("pesce" if lingua == "it" else "fish"):
            animale = Pesce(nome, lingua)
        elif specie == ("pappagallo" if lingua == "it" else "parrot"):
            animale = Pappagallo(nome, lingua)
        else:
            print(msg["specie_err"])
            continue  # torna a chiedere la specie

        while True: # selezione interazione
            continua = input(msg["act"].format(nome=nome)).lower()
            if continua == "n":
                animale.exit()
                return # chiude il gioco
            elif continua == "y":
                while True:
                    ordine = input(msg["comand"]).lower()
                    if ordine in ["parla", "1", "speak"]:
                        animale.parla()
                        print("")
                    elif ordine in ["seduto", "2", "sit"]:
                        animale.seduto()
                        print("")
                    elif ordine in ["terra", "3", "down"]:
                        animale.terra()
                        print("")
                    elif ordine in ["bravo", "4", "good"]:
                        animale.bravo()
                        print("")
                    elif ordine in ["biscotto", "5", "treat"]:
                        animale.biscotto()
                        print("")
                    elif ordine in ["osserva", "6", "look"]:
                        animale.osserva()
                        print("")
                    elif ordine in ["vado via", "7", "go away"]:
                        animale.exit()
                        return # chiude il gioco
                    else:
                        print(msg["confused"].format(nome=nome))
                        continue # torna alle opzioni "ordine"
            else:
                print(msg["error"])
                continue # torna alle opzioni "ordine"

il_mio_animale() # avvio gioco