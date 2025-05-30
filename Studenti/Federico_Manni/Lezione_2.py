# print ("Calcolatrice")

# num1 = float(input("dimmi il primo numero: "))
# num2 = float(input("dimmi il secondo numero: "))
# operazione = input("dimmi l'operazione da eseguire (+, -, *, /): ")

# print("----------------")

# if operazione == "+":
#     print("il risultato è ", num1 + num2)
# elif operazione == "-":
#     print("il risultato è ", num1 - num2)
# elif operazione == "*":
#     print("il risultato è ", num1 * num2)
# elif operazione == "/":
#     print("il risultato è ", num1 / num2)
# else:
#     print("Operazione non valida")


print("----------------") 

print("calcolatrice 2")
num1 = float(input("Dimmi il primo numero: "))
num2 = float(input("Dimmi il secondo numero: "))
operazione = input("Dimmi l'operazione da eseguire (+, -, *, /): ")

def calcolo(num1, num2, operazione):
    if operazione == "+":
        return num1 + num2
    elif operazione == "-":
        return num1 - num2
    elif operazione == "*":
        return num1 * num2
    elif operazione == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Errore: divisione per zero"
    else:
        return "Operazione non valida"
    
result = calcolo(num1, num2, operazione)
print ("Il risultato è:", (result))

print("-----------------")

"""
print("calcolatrice 3")

numero1 = float(input("dimmi il primo numero "))
numero2 = float(input("dimmi il secondo numero "))
operazione = (input("dimmi l'operazione che vuoi effettuare, + - : / ")) 

def calcolo():
    if operazione == "+":
        return numero1 + numero2
    elif operazione == "-":
        return numero1 - numero2
    elif operazione == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Errore: divisione per zero"
    elif operazione == "*":
        return numero1 * numero2
    else:
        return "Operazione non valida"
    
result = calcolo()
print("il risultato è:\n", result)
"""
