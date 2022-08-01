dinheiro = int(input('Quanto você quer sacar? '))
total = dinheiro
cel50 = 0
cel20 = 0
cel10 = 0
cel01 = 0

while total != 0:
    if total >= 50:
        total = total - 50
        cel50 += 1
    elif 50 > total >= 20:
        total = total - 20
        cel20 += 1
    elif 20 > total >= 10:
        total = total - 10
        cel10 += 1
    elif 10 > total >= 1:
        total = total - 1
        cel01 += 1

if cel50 > 0:
    print('Total de {} cédulas de R$50'.format(cel50))
if cel20 > 0:
    print('Total de {} cédulas de R$20'.format(cel20))
if cel10 > 0:
    print('Total de {} cédulas de R$10'.format(cel10))
if cel01 > 0:
    print('Total de {} cédulas de R$01'.format(cel01))