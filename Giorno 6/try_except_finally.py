print("eseguo la divisione")
numero_1 = input("dimmi il primo numero: ")  
numero_2 = input("dimmi il secondo numero: ")
try:
    divisione = float(numero_1) / float(numero_2)
    print(f"la divisione è {divisione}\n")
except ZeroDivisionError:
    print("non si può inserire zero")
finally:
    print("chiusura del programma...")

print("tutto è andato bene, il programma è terminato")