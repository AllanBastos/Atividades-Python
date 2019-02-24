lista = [int(i) for i in input().split()]
arroz = lista[:]
lista.sort()
for i in range(3):
    print(lista[i])

print()

for i in range(3):
    print(arroz[i])

