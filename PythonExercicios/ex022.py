n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}'.format(n.upper()))
print('Seu nome em letras minúsculas é {}'.format(n.lower()))
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(n.split()[0])))
