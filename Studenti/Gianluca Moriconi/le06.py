#esercizio 1

lista_nomi = []

def ins_nomi():
    for i in range(5):
        nome = input("Inserisci un nome: ")
        lista_nomi.append(nome)
    
ins_nomi()
print(lista_nomi)

nomi_miei = lista_nomi.copy()

nomi_miei.append("Gianluca")
nomi_miei.insert(2, "Luca")
print(nomi_miei)

nomi_miei.remove("Luca")
print(nomi_miei)

nome_tolto = nomi_miei.pop(0)
print(f"Il nome tolto è: {nome_tolto}")