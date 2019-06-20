import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Terceiro aluno: '))
todos = [a1, a2, a3, a4]
random.shuffle(todos)
print('A ordem da apresentação do trabalho será:\n{}'.format(todos))
