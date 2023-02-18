numero1 = int(input('1- Digite um número: '))
numero2 = int(input('2- Digite um número: '))
numero3 = int(input('3- Digite um número: '))
numero4 = int(input('4- Digite um número: '))

tupla = (numero1, numero2, numero3, numero4)

#a) Quantas vezes apareceu o valor 9
print('O 9 apareceu: ', tupla.count(9))

#b) Em que posição foi digitado o primeiro valor 3
if tupla.count(3) == 0:
    print('O número 3 não está na lista')
else:
    print('O primeiro valor 3 foi digitado na posição: ', tupla.index(3, 0, 4))

#c) Quais foram os números pares
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print('Par: ', tupla[c])
