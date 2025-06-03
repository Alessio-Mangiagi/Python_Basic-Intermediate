lista = ["\nprova","\nok"]
with open("prova.txt", "a", encoding="utf-8") as f:
    f.writelines(lista)
    f.close()
