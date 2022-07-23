velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7.00
    print('Você foi multado no valor de: R${}'.format(multa))
else:
    print('Tudo tranquilo. Tenha um bom dia')