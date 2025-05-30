def calcolatrice(): 
    print("Benvenuto")
    decisione = input("Scegli un'operazione:\n(1) Somma\n)2) Sottrazione\n(3) Moltiplicazione\n(4) Divisione\n")
    
    if decisione == "1":
        print("eseguo la somma")
        numero_1 = input("dimmi il primo numero: ")  
        numero_2 = input("dimmi il secondo numero: ") 
        somma = float(numero_1) + float(numero_2 )
        print(f"la somma è {somma}\n")   
    elif decisione == "2":
        print("eseguo la sottrazione")
        numero_1 = input("dimmi il primo numero: ")  
        numero_2 = input("dimmi il secondo numero: ") 
        sottrazione = float(numero_1) - float(numero_2)
        print(f"la sottrazione è {sottrazione}\n")
    elif decisione == "3":
        print("eseguo la moltiplicazione")
        numero_1 = input("dimmi il primo numero: ")  
        numero_2 = input("dimmi il secondo numero: ") 
        moltiplicazione = float(numero_1) * float(numero_2)
        print(f"la moltiplicazione è {moltiplicazione}\n")
    elif decisione == "4":
        print("eseguo la divisione")
        numero_1 = input("dimmi il primo numero: ")  
        numero_2 = input("dimmi il secondo numero: ") 
        if numero_2 != "0":
            divisione = float(numero_1) / float(numero_2)
            print(f"la divisione è {divisione}\n")
        else:
            print("non si può inserire zero")
    else: 
        print("il valore inserito non è riconosciuto")

calcolatrice()