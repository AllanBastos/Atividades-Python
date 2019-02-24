'''
from math import trunc
num = input('Digite um valor: ').replace(',', '.')
num = float(num)
print('O valor digitado foi {} e sua porção interira é {}'.format(num, trunc(num)))
'''

num = input('Digite um valor: ').replace(',', '.')
num = float(num)
print('O valor digitado foi {} e sua porção interira é {}'.format(num, int(num)))

