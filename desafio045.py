from random import randint
from time import sleep

jogo = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0,2)

jogador = int(input('[0] Pedra'
                    '\n[1] Papel'
                    '\n[2] Tesoura'
                    '\nDigite o número que corresponde a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('Jogador: {} \nPC: {}'.format(jogo[jogador], jogo[pc]))

if jogador == pc:
    print('Empate')
elif jogador == 0 and pc == 1: #pedra e papel
    print('PC venceu')
elif jogador == 0 and pc == 2: #pedra e tesoura
    print('Jogador venceu')
elif jogador == 1 and pc == 0: #papel e pedra
    print('Jogador venceu')
elif jogador == 1 and pc == 2: #papel e tesoura
    print('PC venceu')
elif jogador == 2 and pc == 0: #tesoura e pedra
    print('PC venceu')
elif jogador == 2 and pc == 1: #tesoura e papel
    print('Jogador venceu')