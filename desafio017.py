from math import hypot
catetoOposto = float(input('Cateto oposto: '))
catetoAdjacente = float(input('Cateto adjacente: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('Cateto oposto: {}'
      '\nCateto adjacente: {}'
      '\nHipotenusa: {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))