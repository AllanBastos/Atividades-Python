'''
def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3


n1 = int(input('Primerio valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print('O menor valor digitado foi {}'.format(menor(n1, n2, n3)))
print('O maior valor digitado foi {}'.format(maior(n1, n2, n3)))
'''


lista = []
n1 = lista.append(int(input('Primerio valor: ')))
n2 = lista.append(int(input('Segundo valor: ')))
n3 = lista.append(int(input('Terceiro valor: ')))

lista.sort()

menor = lista[0]
maior = lista[-1]
print('O menor valor é {}.'.format(menor))
print('O maior valor é {}.'.format(maior))
