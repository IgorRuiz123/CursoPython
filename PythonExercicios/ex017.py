import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(math.hypot(co, ca)))