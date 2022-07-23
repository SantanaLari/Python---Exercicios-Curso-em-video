nome = input('Digite o nome completo: ')

print('Maiuscula: ', nome.upper())
print('Minuscula: ', nome.lower())
print('Total de letras: ', len(''.join(nome.split())))
print('Primeiro nome: ', nome.split()[0],
     'e total de letras: ', len(nome.split()[0]))
