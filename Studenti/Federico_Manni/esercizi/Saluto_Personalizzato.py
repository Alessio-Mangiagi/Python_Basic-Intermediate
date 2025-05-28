
#! Saluto personalziato con nome e eta

# nome = input("Dimmi il tuo nome per favore: ")
# eta = input("Dimmi la tua eta per favore: ")


# def validazione(nome, eta):
#     if nome.strip() == "":
#         return "Il nome non può essere vuoto."
#     elif eta.strip() == " ":
#         return "L'età non può essere vuota."
#     elif eta.isdigit() == False:
#         return "L'età deve essere un numero."
#     else:
#         return f"Ciao {nome}, hai {eta} anni!"

# print(validazione(nome, eta))

nome = input("Dimmi il tuo nome per favore: ")
if nome.strip() == "":
    print("Il nome non può essere vuoto.")
elif nome.isdigit() == True:
    print("Il nome non può essere composto solo da numeri.")
else:
    eta = input("Dimmi la tua età per favore: ")
    if eta.strip() == "":
        print("L'età non può essere vuota.")
    elif eta.isdigit() == False:
        print("L'età deve essere un numero.")
    else:
        print( f"Ciao {nome}, hai {eta} anni!")
