import time 
import numpy as np
import sys 

# Print ritardato

def print_ritardato(s):
    # stampa un carattere alla volta 
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creiamo la classe

class Pokemon:
    def __init__ (self, name, types, moves, EVs, health='==================='):
        # Salviamo le informazioni del Pokemon
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs["ATTACCO"]
        self.defense = EVs["DIFESA"]
        self.health = health
        self.bars = 20 # Numero di barre di salute

    def fight(self, Pokemon2):
        # Permette di combattere contro un altro Pokemon

        # Stampiamo informazioni sulla lotta
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TIPO/", self.types)
        print(f"ATTACCO/ {self.attack}")
        print(f"DIFESA/ {self.defense}")
        print(f"LIVELLO/", 3*(1+np.mean([self.attack, self.defense])))
        print(f"\nVS")
        print(f"\n{Pokemon2.name}")
        print("TIPO/", Pokemon2.types)
        print(f"ATTACCO/ {Pokemon2.attack}")
        print(f"DIFESA/ {Pokemon2.defense}")
        print(f"LIVELLO/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # Consideriamo i tipi dei Pokemon 
        version = ["Fuoco", "Acqua", "Erba"]
        for i,k in enumerate(version):
            if self.types == k:
            # Se entrambi i Pokemon hanno lo stesso tipo
                if Pokemon2.types == k:
                    string_1_attack = "Non è molto efficace..."
                    string_2_attack = "Non è molto efficace..."
            
            # Pokemon2 è più forte
            if Pokemon2.types == version[(i+1)%3]:
                Pokemon2.attack *= 2
                Pokemon2.defense *= 2
                self.attack /= 2
                self.defense /= 2
                string_1_attack = "\nÈ superefficace!"
                string_2_attack = "\nNon è molto efficace..."

            # Pokemon2 è più debole
            if Pokemon2.types == version[(i+2)%3]:
                self.attack *= 2
                self.defense *= 2
                Pokemon2.attack /= 2
                Pokemon2.defense /= 2
                string_1_attack = "\nNon è molto efficace..."
                string_2_attack = "\nÈ superefficace!"

            
        # Per la lotta attuale...
        # Continua fino a quando il pokemon ha salute
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Stampa le barre di salute
            print(f"{self.name}\t\tHLTH\{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\{Pokemon2.health}\n")

            print(f"VAI {self.name}!") 
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Seleziona una mossa: ")) 
            print_ritardato(f"{self.name} usa {self.moves[index-1]}!\n")
            time.sleep(1)
            print_ritardato(string_1_attack)
                        
            # Determiniamo i danni
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Aggiungiamo le barre di salute
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="
                        
            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\{Pokemon2.health}\n")
            time.sleep(.5)

            # Controlliamo se qualche Pokemon è stato sconfitto
            if Pokemon2.bars <= 0:
                print_ritardato(f"\n...{Pokemon2.name} è stato sconfitto!")
                break

            # Il turno di Pokemon2

            print(f"VAI {Pokemon2.name}!") 
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input("Seleziona una mossa: ")) 
            print_ritardato(f"{Pokemon2.name} usa {Pokemon2.moves[index-1]}!\n")
            time.sleep(1)
            print_ritardato(string_2_attack)
                        
            # Determiniamo i danni
            self.bars -= self.attack
            self.health = ""

            # Aggiungiamo le barre di salute
            for j in range(int(self.bars+.1*self.defense)):
                            self.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\{Pokemon2.health}\n")
            time.sleep(.5)

            # Controlliamo se qualche Pokemon è stato sconfitto
            if self.bars <= 0:
                print_ritardato(f"\n...{self.name} è stato sconfitto!")
                break

            money = np.random.choice(5000)
            print_ritardato(f"\nHai vinto {money} monete!\n")






if __name__ == "__main__":
# Creiamo i Pokemon
    Charmander = Pokemon("Charmander", "Fuoco", ["Lanciafiamme", "Fuocopugno", "Braciere", "Rogodenti"], {"ATTACCO": 52, "DIFESA": 43})
    Squirtle = Pokemon("Squirtle", "Acqua", ["Idropompa", "Idrocannone", "Acquagetto", "Idrogetto"], {"ATTACCO": 48, "DIFESA": 65})
    Bulbasaur = Pokemon("Bulbasaur", "Erba", ["Foglielama", "Velenpuntura", "Frustata", "Raffica"], {"ATTACCO": 49, "DIFESA": 49})

    Charmeleon = Pokemon("Charmeleon", "Fuoco", ["Lanciafiamme", "Fuocopugno", "Braciere", "Rogodenti"], {"ATTACCO": 64, "DIFESA": 58})
    Wartortle = Pokemon("Wartortle", "Acqua", ["Idropompa", "Idrocannone", "Acquagetto", "Idrogetto"], {"ATTACCO": 63, "DIFESA": 80})
    Ivysaur = Pokemon("Ivysaur", "Erba", ["Foglielama", "Velenpuntura", "Frustata", "Raffica"], {"ATTACCO": 62, "DIFESA": 63})

    Charizard = Pokemon("Charizard", "Fuoco", ["Lanciafiamme", "Fuocopugno", "Braciere", "Rogodenti"], {"ATTACCO": 84, "DIFESA": 78})
    Blastoise = Pokemon("Blastoise", "Acqua", ["Idropompa", "Idrocannone", "Acquagetto", "Idrogetto"], {"ATTACCO": 83, "DIFESA": 100}) 
    Venusaur = Pokemon("Venusaur", "Erba", ["Foglielama", "Velenpuntura", "Frustata", "Raffica"], {"ATTACCO": 82, "DIFESA": 83})

x = True
while x:
    Charmander.fight(Blastoise)
    print("\nVuoi combattere ancora? (S/N)")
    choice = input().strip().upper()
    if choice != "S":
        x = False
        print("Grazie per aver giocato!")
    else:
        print("Inizia una nuova lotta!")