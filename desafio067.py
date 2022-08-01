num = 0

while True:
    cont = 0
    num = int(input('Digite um valor: '))

    if num < 0:
        break

    while cont <= 10:
        print('{} x {} = {}'.format(num, cont, num*cont))
        cont += 1
