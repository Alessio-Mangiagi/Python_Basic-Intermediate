def calcolatrice():
    print("benvenuto")
    x = True
    while x:
3        decisione = input("Scegli un'operazione:\n(1) Somma\n(2) Sottrazione\n(3) Moltiplicazione\n(4) Divisione\n")
        if decisione == "1":
            print("eseguo la somma")
            numero_1 = input("dimmi il primo numero:") 
            numero_2 = input("dimmi il secondo numero:")
            somma = float(numero_1) + float(numero_2)
            print(f"la somma è {somma}\n")
        elif decisione == "2":
            print("eseguo la sottrazione")
            numero_1 = input("dimmi il primo numero:") 
            numero_2 = input("dimmi il secondo numero:")
            sottrazione = float(numero_1) - float(numero_2)
            print(f"la sottrazione è {sottrazione}\n")
        elif decisione == "3":
            print("eseguo la moltiplicazione")
            numero_1 = input("dimmi il primo numero:") 
            numero_2 = input("dimmi il secondo numero:")
            moltiplicazione = float(numero_1) * float(numero_2)
            print(f"la moltiplicazione è {moltiplicazione}\n")
        elif decisione == "4":
            print("eseguo la divisione")
            numero_1 = input("dimmi il primo numero:") 
            numero_2 = input("dimmi il secondo numero:")
            if float(numero_2) != 0:
                divisione = float(numero_1) / float(numero_2)
                print(f"la divisione è {divisione}\n")
            else:
                print("non si può inserire 0")
        else:    
            print("il valore inserito non è stato riconosciuto")
        continua = input("vuoi eseguire un'altra operazione? (si/no): ")   
        if continua.lower() == "no":
            x = False
            print("grazie per aver usato la calcolatrice")
        elif continua.lower() != "si":
            x = False
            print("grazie per aver usato la calcolatrice")
        else: 
            x = True
            print("continuiamo con la calcolatrice")    

calcolatrice()







