def nome_maisc(nome,eta):
    return nome.upper(), eta 

x=True
while x:
    nome = input("Inserisci il tuo nome: ")
    eta = input("Inserisci la tua età: ")
    
    persona= nome_maisc(nome, eta)
    
    print(f"Il tuo nome in maiuscolo è: {persona[0]} e la tua età è: {persona[1]} anni.")
    
    continua = input("Vuoi inserire un altro nome? (s/n): ")
    if continua.lower() != 's':
        x = False
        print("Grazie per aver usato il programma!")
  