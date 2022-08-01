n = 0
cont = 0
soma = n

while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break

    cont += 1
    soma = soma + n


print('Quantidade de numeros digitados: ', cont)
print('Soma: ', soma)