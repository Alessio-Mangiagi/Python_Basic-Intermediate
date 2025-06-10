import datetime
from utils import check_ore_digiuno, esci_programma

# Intermittent Fasting Calculator
# Questo programma calcola l'ora in cui puoi mangiare dopo un periodo di digiuno.
class IntermittentFastingCalculator:
    def __init__(self, ore_digiuno=0, ora_finito_mangiare=0, minuti_finito_mangiare=0, ora_che_puoi_mangiare=0):
        self.ore_digiuno = ore_digiuno
        self.ora_finito_mangiare = ora_finito_mangiare
        self.minuti_finito_mangiare = minuti_finito_mangiare
        self.ora_che_puoi_mangiare = ora_che_puoi_mangiare
        self.__x = True
        self.__y = True
    # Metodo per calcolare l'ora in cui puoi mangiare
    # Chiede all'utente l'ora e i minuti in cui ha finito di mangiare
    def calcola_ora_mangiare(self):

        while self.__x:
            try:
                self.ore_digiuno = int(input("Quante ore vuoi digiunare? (Inserisci un numero da 0 a 24): "))
                if check_ore_digiuno(self.ore_digiuno):
                    continue

                self.ora_finito_mangiare = int(input("A che ora hai finito di mangiare? "))
                self.minuti_finito_mangiare = int(input("E quanti minuti? "))
                h = 24 - self.ore_digiuno
                self.ora_che_puoi_mangiare = (self.ora_finito_mangiare - h) % 24
                print(f"Puoi mangiare alle {self.ora_che_puoi_mangiare:02d}:{self.minuti_finito_mangiare:02d}.")
                self.__y = True
            except ValueError:
                print("Per favore, inserisci valori numerici validi.")
                continue
            except Exception as e:
                print(f"Si è verificato un errore: {e}. Per favore, riprova.")
                continue
            # Chiede se l'utente vuole fare un'altra operazione
            self.__x = esci_programma(self.__x, self.__y)      
    
    
        

if __name__ == "__main__":
    fasting = IntermittentFastingCalculator()
    fasting.calcola_ora_mangiare()

            