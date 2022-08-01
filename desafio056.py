media = 0
maisVelho = 0
nomeVelho = ''
menos20 = 0


for c in range(1, 5):
    print('==== {} pessoa ===='.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    media += (idade/4)

    if sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    if sexo == 'F' and idade < 20:
        menos20 += 1

print('Media: ', media, ' anos')
print('Homem mais velho: ', nomeVelho, ' com ', maisVelho, ' anos')
print('Total de mulheres com menos de 20 anos: ', menos20)

