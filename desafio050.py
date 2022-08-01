soma = 0

for c in range(0,6):
    valor = int(input('{} - Digite um numero: '.format(c)))
    if valor % 2 == 0:
        soma = valor + soma

print(soma)