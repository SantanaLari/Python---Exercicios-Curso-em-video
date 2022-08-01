valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Salario: '))
anos = int(input('Em quantos anos vai pagar: '))

prestacao = valorCasa/(anos*12)
verificacao = salario * 0.30

print('Valor da prestação: ', prestacao)

if verificacao >= prestacao:
    print('Emprestimo efetivado')
else:
    print('Emprestimo recusado')
