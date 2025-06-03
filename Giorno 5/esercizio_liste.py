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

nomi_miei.remove("Luca")
print(nomi_miei)

nome_tolto = nomi_miei.pop(0)
print(f"Il nome tolto è: {nome_tolto}")