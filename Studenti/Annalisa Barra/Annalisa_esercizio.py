numeri = [5,10,4,2,4,6,8]
for n in numeri:
    if n >= 6:
        print(f"{n} è maggiore o uguale a 6")
    else:
        numeri.remove(n)
        n = n + 2
        print(f"{n} è minore di 6, quindi viene incrementato di 2")

        print(numeri)
