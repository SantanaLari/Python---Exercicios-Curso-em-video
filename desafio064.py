n = 0
totalDigitado = 0
soma = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        totalDigitado += 1
        soma = soma + n

print('Total de numeros digitados: ', totalDigitado,
      '\nSomatoria: ', soma)