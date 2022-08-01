val1 = int(input('Digite um numero: '))
val2 = int(input('Digite outro numero: '))

if val1 > val2:
    print('O primeiro valor ({}) é maior'.format(val1))
elif val2 > val1:
    print('O segundo valor ({}) é maior.'.format(val2))
else:
    print('Não existe valor maior, os dois são iguais')