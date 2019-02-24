total = int(input())

print("{}".format(total))

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while total >= 100:
    notas100 += 1
    total -= 100

while total >= 50:
    notas50 += 1
    total -= 50

while total >= 20:
    notas20 += 1
    total -= 20

while total >= 10:
    notas10 += 1
    total -= 10

while total >= 5:
    notas5 += 1
    total -= 5

while total >= 2:
    notas2 += 1
    total -= 2

while total >= 1:
    notas1 += 1
    total -= 1

print('{} nota(s) de R$ 100,00'.format(notas100))
print('{} nota(s) de R$ 50,00'.format(notas50))
print('{} nota(s) de R$ 20,00'.format(notas20))
print('{} nota(s) de R$ 10,00'.format(notas10))
print('{} nota(s) de R$ 5,00'.format(notas5))
print('{} nota(s) de R$ 2,00'.format(notas2))
print('{} nota(s) de R$ 1,00'.format(notas1))