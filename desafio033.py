val1 = int(input('Digite um numero: '))
val2 = int(input('Digite um numero: '))
val3 = int(input('Digite um numero: '))

if val1 > val2 and val1 > val3:
    print('Maior: {}'.format(val1))
elif val2 > val1 and val2 > val3:
    print('Maior: {}'.format(val2))
else:
    print('Maior: {}'.format(val3))

if val1 < val2 and val1 < val3:
    print('Menor: {}'.format(val1))
elif val2 < val1 and val2 < val3:
    print('Menor: {}'.format(val2))
else:
    print('Menor: {}'.format(val3))
