s = input('Informe seu sexo: [M/F] ').upper()

while s != 'M' and s != 'F':
    s = input('Dados invalidos. Informe seu sexo: ').upper()

print('Sexo {} registrado com sucesso'.format(s))
