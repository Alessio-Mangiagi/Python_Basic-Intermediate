def nome_maiuscolo(nome, eta):
    return nome.upper(), eta                                  #.upper per convertire il nome in maiuscolo

x = True                                                      #inizializzo la variabile x a True per entrare nel ciclo while
while x:                                                      #il ciclo while continua finché x è True       
    nome = input("Nome:")
    eta = input("Età:")
    persona = nome_maiuscolo(nome, eta)                       #a persona è associata una tupla con nome e età
    print(f"Il nome è: {persona[0]} e l'età è: {persona[1]}") #stampo il nome e l'età  
    
    y = True                                                  #inizializzo la variabile y a True per entrare nel ciclo while
    while y:
        print("vuoi continuare? (s/n)")                       #chiedo se si vuole continuare
        risposta = input().lower()                            # prendo l'input e lo converto in minuscolo
        if risposta == 'n':                                   #se l'input è n
            x = False
            y = False
        elif risposta == 's':                                 #se l'input è s   
            y = False
            print("\n\n\n")
        else:                                                 #se l'input non è n o s               
            print("\n\n\n")