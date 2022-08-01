continuar = ''
maioridade = 0
homens = 0
m20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Sexo: [M/F]').upper()

    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        m20 += 1

    continuar = input('Quer continuar? [S/N]').upper()
    if continuar == 'N':
        break

print('Maiores de idade: {} pessoas'.format(maioridade))
print('Homens cadastrados: {}'.format(homens))
print('Mulheres com menos de 20 anos: {}'.format(m20))