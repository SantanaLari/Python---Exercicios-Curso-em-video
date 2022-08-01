continuar = 'S'
total = 0
maior1000 = 0
cont = 0
precoB = 0
produtoB = ''

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Preco: '))
    total = total + preco
    cont += 1

    if preco > 1000.00:
        maior1000 += 1

    if cont == 1:
        precoB = preco
        produtoB = nome
    else:
        if preco < precoB:
            precoB = preco
            produtoB = nome

    continuar = input('Continuar? [S/N] ').upper()
    if continuar == 'N':
        break

print('Total gasto: {} \nProdutos acima de 1000.00: {}'
      '\nProduto mais barato: {}'.format(total, maior1000, produtoB))