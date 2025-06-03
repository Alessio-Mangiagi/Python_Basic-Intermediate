lista = []

for n in range(5):
    nomi = input("Inserisci un nome: ")
    lista.append(nomi)

print(lista)

print("-------------")

nomi_miei = lista.copy()

nomi_miei.append("luca")
nomi_miei.insert(2, "Marco")
print(nomi_miei)