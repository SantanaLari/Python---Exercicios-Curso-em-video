preco = float(input('Preco: '))
condicao = int(input('1- à vista dinheiro/cheque'
                     '\n2- à vista no cartao'
                     '\n3- em ate 2x no cartao'
                     '\n4- 3x ou mais no cartao'
                     '\nInsira a sua escolha: '))

if condicao == 1:
    valor = preco-(preco*0.10)
elif condicao == 2:
    valor = preco-(preco*0.05)
elif condicao == 3:
    valor = preco
elif condicao == 4:
    parcelas = int(input('Informe o valor das parcelas: '))
    valor = preco + (preco * 0.20)
    calculoParcelado = valor/parcelas
    print('Compra parcelada em {}x de R${}'.format(parcelas, calculoParcelado))

print('Preco final: ', valor)