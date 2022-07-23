salario = float(input('Digite o salario: '))

if salario > 1250.00:
    aumento = (salario*0.10)+salario
else:
    aumento = (salario*0.15)+salario

print('Salario: {}\nSalario com aumento: {}'.format(salario, aumento))
