import math
angulo = float(input('Angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Angulo: {} \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'
      .format(angulo, seno, cosseno, tangente))