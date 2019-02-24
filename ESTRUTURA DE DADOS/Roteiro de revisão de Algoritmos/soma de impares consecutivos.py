n = int(input())

for i in range(n):
    x, y = (input()).split()
    x, y = int(x), int(y)

    soma = 0
    for c in range(x, x + y*2):
        if c % 2 != 0:
            soma += c
    print(soma)


