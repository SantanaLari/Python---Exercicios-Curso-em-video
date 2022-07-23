a = float(input('Ponha um comprimento: '))
b = float(input('Ponha um comprimento: '))
c = float(input('Ponha um comprimento: '))

cond1 = b - c
cond2 = a - c
cond3 = a - b

if cond1 < a < (b+c) and cond2 < b < (a+c) and cond3 < c < (a+b):
    print('Pode-se formar um triângulo')
else:
    print('Não se pode formar um triângulo')
