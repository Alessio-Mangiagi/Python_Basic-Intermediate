def nome_maiusc(nome, età):
    return nome.upper(), età

x = True
while x:
    nome = input("Inserisci il tuo nome: ")
    età = input("Inserisci la tua età: ")
    persona = nome_maiusc(nome, età)
    print(f"il nome è: {persona[0]} e l'età è: {persona[1]} anni")
    print("Vuoi inserire un altro nome? (s/n)")
    risposta = input().lower()
    if risposta != 's':
        x = False