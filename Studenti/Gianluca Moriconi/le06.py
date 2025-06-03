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
nomi_miei.insert(2, "Mario")
print(nomi_miei)