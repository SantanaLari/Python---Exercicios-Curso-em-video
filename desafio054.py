from datetime import date

anoAtual = date.today().year

maior = 0
menor = 0

for c in range(0, 6):
    nasc = int(input('Digite o ano de nascimento: '))
    if anoAtual - nasc >= 18:
        maior += 1
    else:
        menor += 1

print('Maiores de idade: {} pessoa(s) \nMenores de idade: {} pessoa(s)'.format(maior, menor))

