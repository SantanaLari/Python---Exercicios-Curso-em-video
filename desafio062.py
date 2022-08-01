termo1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
res = termo1
cont = 1
qtdTermo = 1

while cont <= 10:
    print(res)
    res += r
    cont += 1

while qtdTermo != 0:
    mostrar = 0
    qtdTermo = int(input('Quantos termos você quer mostrar? '))
    while mostrar < qtdTermo:
        print(res)
        res += r
        mostrar += 1
