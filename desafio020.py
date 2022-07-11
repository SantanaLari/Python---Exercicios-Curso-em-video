from random import shuffle

n1 = input('Aluno1: ')
n2 = input('Aluno2: ')
n3 = input('Aluno3: ')
n4 = input('Aluno4: ')

aluno = [n1, n2, n3, n4]
shuffle(aluno)

print(aluno)