import random
lista = []
for i in range(1, 5):
    alunos = input('Aluno {}: '.format(i))
    lista.append(alunos)
print('O Aluno escolhido foi: {} '.format(random.choice(lista)))