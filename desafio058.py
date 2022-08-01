from random import randint
pc = randint(0, 10)
palpite = 1

print('Estou pensando em um numero entre 0 e 10.'
      'Em qual número estou pensando? ')

user = int(input('Digite seu primeiro palpite: '))

if user == pc:
    print(end='')
else:
    while user != pc:
        print('Você errou. Tente novamente')
        user = int(input('Digite seu palpite: '))
        palpite += 1

print('Você acertou e deu {} palpites até vencer'.format(palpite))