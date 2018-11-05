def fat(n):
    if n == 1:
        return 1
    return n*fat(n-1)


lista = []
multiplos3 = 0
for i in range(5):
    n = int(input())

    if n % 3 == 0:
        multiplos3 += fat(n)

print(multiplos3)

