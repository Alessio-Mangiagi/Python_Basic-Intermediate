def nome_maiuscolo(nome, eta):
    return f"\nIl nome è: {nome.upper()}, l' età è: {eta}" #.upper per convertire il nome in maiuscolo

x = True #inizializzo la variabile x a True per entrare nel ciclo while
while x: #il ciclo while continua finché x è True       
    nome = input("Nome:")
    eta = input("Età:")
    persona = nome_maiuscolo(nome, eta)
    print(persona)
    
    y = True
    while y:
        print("vuoi continuare? (s/n)")
        risposta = input().lower()
        if risposta == 'n':
            x = False
            y = False
        elif risposta == 's':
            y = False
            print("\n\n\n")
        else:
            print("\n\n\n")