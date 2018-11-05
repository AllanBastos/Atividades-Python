import random
lista = []
for i in range(1, 5):
    nomes = input('Aluno {}: '.format(i)).strip()
    lista.append(nomes)
random.shuffle(lista)
print('A ordem de Apresentação será')
for l in range(len(lista)):
    if l != (len(lista)-1):
        print(str(l+1)+'°:', lista[l], end='\n')
    else:
        print(str(l+1)+'°:', lista[l], end='.')
