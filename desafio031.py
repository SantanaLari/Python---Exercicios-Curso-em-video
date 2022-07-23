distancia = float(input('Digite a distancia da viagem: '))
print('{}km'.format(distancia))

if distancia <= 200:
    passagem = distancia * 0.50
    print('Passagem: RS{}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Passagem: RS{}'.format(passagem))