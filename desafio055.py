maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Digite um peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('Maior peso: {} \nMenor peso: {}'.format(maior, menor))