numero = input('Digite um número entre 0 a 9999: ')

total = len(numero)

if total == 4:
    print('Unidade: {}'.format(numero[3]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))
elif total == 3:
    print('Unidade: {}'.format(numero[2]))
    print('Dezena: {}'.format(numero[1]))
    print('Centena: {}'.format(numero[0]))
elif total == 2:
    print('Unidade: {}'.format(numero[1]))
    print('Dezena: {}'.format(numero[0]))
else:
    print('Unidade: {}'.format(numero[0]))