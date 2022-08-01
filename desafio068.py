from random import randint
vitoria = 0

while True:
    parImpar = input('Você quer ser Par [P] ou Impar [I]? ').upper()
    valor = randint(0,100)
    if parImpar == 'P':
        if valor % 2 == 0:
            print('{} é par. O jogador venceu.'.format(valor))
            vitoria += 1
        else:
            print('{} é impar. O jogador perdeu'.format(valor))
            break
    elif parImpar == 'I':
        if valor % 2 == 0:
            print('{} é par. O jogador perdeu.'.format(valor))
            break
        else:
            print('{} é impar. O jogador venceu'.format(valor))
            vitoria += 1
    else:
        print('Valor incorreto. Tente novamente')

print('Total de vitorias: ', vitoria)