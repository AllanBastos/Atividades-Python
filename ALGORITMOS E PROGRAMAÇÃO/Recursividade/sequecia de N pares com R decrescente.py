def pares(x):
    if x == 1:
        return 0

    for i in range(x, 0-1,-1):
        if i % 2 == 0:
            print(i)

n = int(input())
(pares(n))