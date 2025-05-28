
#Funzione del nostro convertitore di temperatura 
def convertitore_temp():
    print("Benvenuto nel convertitore di temperatura!")
    tipo_temp = input("Premi il tasto:\nC. per convertire da Fahrenheit a Celsius\nF. per convertire da Celsius a Fahrenheit\noppure digita 'exit' per uscire: ").strip().lower()
    if tipo_temp == 'exit':
        print("Chiusura del convertitore in corso... Alla prossima!")
        return
    elif tipo_temp == 'c':
        fahrenheit = float(input("Inserisci la temperatura in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"La temperatura in Celsius è: {celsius:.2f}°C")
    elif tipo_temp == 'f':
        celsius = float(input("Inserisci la temperatura in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"La temperatura in Fahrenheit è: {fahrenheit:.2f}°F")
    else:
        print("Ehm... Hai sbagliato qualcosa. Riprova!")

convertitore_temp()  