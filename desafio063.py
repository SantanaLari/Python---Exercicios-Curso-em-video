n = int(input('Digite um valor: '))
termo1 = 0
termo2 = 1
cont = 3

if n == 1:
    print(termo1)
elif n == 2:
    print(termo1, termo2)
elif n > 2:
    print(termo1)
    print(termo2)
    while cont <= n:
        termo3 = termo1 + termo2
        print(termo3)
        termo1 = termo2
        termo2 = termo3
        cont += 1

