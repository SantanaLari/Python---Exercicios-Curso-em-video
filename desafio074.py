from random import randint

elemento1 = randint(1, 100)
elemento2 = randint(1, 100)
elemento3 = randint(1, 100)
elemento4 = randint(1, 100)
elemento5 = randint(1, 100)

tupla = (elemento1, elemento2, elemento3, elemento4, elemento5)

print(tupla)
print('Maior valor: ', max(tupla))
print('Menor valor: ', min(tupla))
