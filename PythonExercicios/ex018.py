import math
ang = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Sen: {:.2f} \nCos: {:.2f} \nTan: {:.2f}'.format(seno, cosseno, tangente ))
