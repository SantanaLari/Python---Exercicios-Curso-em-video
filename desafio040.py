n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
media = (n1+n2)/2
print('Media: ', media)

if media < 5.0:
	print('Reprovado')
elif 5.0 <= media <= 6.9:
	print('Recuperação')
else:
	print('Aprovado')