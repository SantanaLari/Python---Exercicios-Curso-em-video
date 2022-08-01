continuar = 'S'
media = 0
cont = 0
maior = menor = 0

while continuar != 'N':
    n = int(input('Digite um numero: '))
    continuar = input('Continuar? [S/N] ').upper()
    cont += 1

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    media = media+n

print('Media: ', media/cont)
print('Maior: ', maior, '\nMenor: ', menor)


