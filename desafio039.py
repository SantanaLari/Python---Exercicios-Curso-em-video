from datetime import date

ano = int(input('Digite o ano de nascimento: '))
verificacao = date.today().year - ano

if verificacao == 18:
    print('Está na hora de se alistar')
elif verificacao < 18:
    print('Ainda falta(m): {} ano(s) para você se alistar'.format(18-verificacao))
else:
    print('Já passou do prazo. Você deveria ter se alistado há {} anos'.format(verificacao-18))