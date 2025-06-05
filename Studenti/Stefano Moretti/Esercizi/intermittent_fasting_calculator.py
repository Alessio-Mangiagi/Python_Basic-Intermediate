import datetime
# Intermittent Fasting Calculator
# Questo programma calcola l'ora in cui puoi mangiare dopo un periodo di digiuno.
class IntermittentFastingCalculator:
    def __init__(self, ore_digiuno=0, ora_finito_mangiare=0, minuti_finito_mangiare=0, ora_che_puoi_mangiare=0):
        self.ore_digiuno = ore_digiuno
        self.ora_finito_mangiare = ora_finito_mangiare
        self.minuti_finito_mangiare = minuti_finito_mangiare
        self.ora_che_puoi_mangiare = ora_che_puoi_mangiare
    # Metodo per calcolare l'ora in cui puoi mangiare
    # Chiede all'utente l'ora e i minuti in cui ha finito di mangiare
    def calcola_ora_mangiare(self):
        x = True
        while x:
            try:
                self.ore_digiuno = int(input("Quante ore vuoi digiunare? (Inserisci un numero da 0 a 24): "))
                if self.ore_digiuno < 0 or self.ore_digiuno > 24:
                    print("Per favore, inserisci un numero tra 0 e 24.")
                    continue
                 
                self.ora_finito_mangiare = int(input("A che ora hai finito di mangiare? "))
                self.minuti_finito_mangiare = int(input("E quanti minuti? "))
                h = 24 - self.ore_digiuno
                self.ora_che_puoi_mangiare = (self.ora_finito_mangiare - h) % 24
                print(f"Puoi mangiare alle {self.ora_che_puoi_mangiare:02d}:{self.minuti_finito_mangiare:02d}.")
                y = True
            except ValueError:
                print("Per favore, inserisci valori numerici validi.")
                continue
            except Exception as e:
                print(f"Si è verificato un errore: {e}. Per favore, riprova.")
                continue
            # Chiede se l'utente vuole fare un'altra operazione
            while y:
                exit = input("Vuoi ancora usare il programma? (S/N) ").lower().strip()
                if exit == 'n':
                    print("Alla prossima!")
                    y = False
                    x = False
                    
                elif exit == 's':
                    x = True
                    y = False
                    continue
                else:
                    print("Per favore, inserisci 'S' o 'N'.")
                    continue

if __name__ == "__main__":
    fasting = IntermittentFastingCalculator()
    fasting.calcola_ora_mangiare()

            