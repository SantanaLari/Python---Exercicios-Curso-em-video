termo1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = termo1 + (10-1)*r

for a in range(termo1, decimo+r, r):
	print(a)