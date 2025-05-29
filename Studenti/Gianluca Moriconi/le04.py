def nome_maiuscolo(nome, eta): #DIFINIZIONE DELLA FUNZIONE
    """Conversione del testo in maiuscolo """ #DOCSTRING - spiegazione della funzione
    return nome.upper(), eta   #VALORE DI RITORNO             #QUANDO LO SCOPE AL'INTERNO DELLA FUNZIONE È LOCALE, LE VARIABILI NON SONO VISIBILI FUORI DALLA FUNZIONE
                                                              #LE VARIABILI USATE NELLE FUNZIONI SONO LOCALI, QUINDI "MUOIONO" DENTRO LA FUNZIONE STESSA
                                                              #IN QUESTO CASO, RICEVE VALORI DALL'ESTERNO, PERCIO' ABBIAMO UNO SCOPE GLOBALE
x = True                                                      #X VARIABILE GLOBALE PRESENTE NEL CORPO DEL PROGRAMMA E NON NELLA FUNZIONE
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