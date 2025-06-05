def calcolatrice(): 
    print("Benvenuto")
    
    x = True

    while x:
        print("inseisci i numeri che vuoi calcolare")
        numero_1 = input("dimmi il primo numero: ")  
        numero_2 = input("dimmi il secondo numero: ") 

        decisione = input("Scegli un'operazione:\n(1) Somma\n(2) Sottrazione\n(3) Moltiplicazione\n(4) Divisione\n")

        if decisione == "1":
            print("eseguo la somma")
            
            somma = float(numero_1) + float(numero_2 )
            print(f"la somma è {somma}\n")   
        elif decisione == "2":
            print("eseguo la sottrazione")
            
            sottrazione = float(numero_1) - float(numero_2)
            print(f"la sottrazione è {sottrazione}\n")
        elif decisione == "3":
            print("eseguo la moltiplicazione")
           
            moltiplicazione = float(numero_1) * float(numero_2)
            print(f"la moltiplicazione è {moltiplicazione}\n")
        elif decisione == "4":
            print("eseguo la divisione")
            
            try: 
                divisione = float(numero_1) / float(numero_2)
                print(f"la divisioneè {divisione}\n")
            except ZeroDivisionError:
                print("non puoi dividere per zero")
        else: 
            print("il valore inserito non è riconosciuto")

        continua = input("Vuoi continuare? (si/no): ").lower()
        if continua == "si":
            print("\n" * 9)
            # x resta True, si continua
        elif continua == "no":
            x = False
            print("\n" * 2)
            print("Grazie per aver usato la calcolatrice!") 
        else:
            print("scusa non ho capito, esco dal programma.")
            x = False

calcolatrice()