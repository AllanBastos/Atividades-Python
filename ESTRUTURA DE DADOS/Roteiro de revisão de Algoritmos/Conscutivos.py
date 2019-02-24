n = int(input())
lista = [i for i in input().split()]

maior = 0
soma = 1

for i in range(n):
    if (lista[i] == lista[i-1]):
        soma += 1
    if i == n-1 or lista[i] != lista[i-1]:
        if soma > maior:
            maior = soma
        soma = 1
print(maior)
