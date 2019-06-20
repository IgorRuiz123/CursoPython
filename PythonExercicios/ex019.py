import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Segundo aluno: '))
a4 = str(input('Terceiro aluno: '))
todos = [a1, a2, a3, a4]
esc = random.choice(todos)
print('O aluno escolhido foi {}'.format(esc))