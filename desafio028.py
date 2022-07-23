from random import randint
pc = randint(0, 5)

print('Estou pensando em um número entre 0 e 5\n'
      'Em que número estou pensando? ')
usuario = int(input('Digite sua resposta: '))

if usuario == pc:
    print('Acertou! Eu estava pensando no número {}'.format(pc))
else:
    print('Errou! Eu pensei no número {} '
          'e você digitou {}'.format(pc, usuario))
