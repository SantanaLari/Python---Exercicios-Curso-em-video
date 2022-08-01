import math

numero = int(input('Digite um valor: '))
print('Base de conversão'
      '\n1 para Binário'
      '\n2 para octal'
      '\n3 para hexadecimal')
base = int(input('Escolha a base de conversão: '))

print('Valor digitado: {}'.format(numero))

if base == 1:
    print('Valor convertido: {}'.format(bin(numero)[2:]))
elif base == 2:
    print('Valor convertido: {}'.format(oct(numero)[2:]))
elif base == 3:
    print('Valor convertido: {}'.format(hex(numero)[2:]))
else:
    print('Opção invalida')