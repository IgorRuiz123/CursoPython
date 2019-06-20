n1 = int(input('Digite um valor: '))
n2: int = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1  // n2
rd = n1 % n2
e = n1 ** n2
print('A soma é {} \nA diferença é {} \nO produto é {} \nA divisão é {:.3f}, '.format(s, sub, m ,d), end='')
print('a  divisão inteira é {}, o resto da divisão é {} \nA potenciação é {}'.format(di, rd, e))