num = int(input('Digite um valor: '))

fat = num
cont = 1

while cont < num:
    fat = fat * cont
    cont += 1

print('Fatorial de {}! = {}'.format(num, fat))
