val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
opc = 0

while opc != 5:
    print('\033[m[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] novos numeros'
          '\n[5] sair')

    opc = int(input('Escolha sua opção: '))

    if opc == 1:
        soma = val1 + val2
        print('\033[31m{} + {} = {}'.format(val1, val2, soma))
    elif opc == 2:
        mul = val1 * val2
        print('\033[31m{} x {} = {}'.format(val1, val2, mul))
    elif opc == 3:
        if val1 > val2:
            print('\033[31mMaior: ', val1)
        else:
            print('\033[31mMaior: ', val2)
    elif opc == 4:
        val1 = int(input('\033[31mDigite um novo valor: '))
        val2 = int(input('\033[31mDigite um novo valor: '))




