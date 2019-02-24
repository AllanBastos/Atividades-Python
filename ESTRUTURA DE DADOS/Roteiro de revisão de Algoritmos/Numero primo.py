n = int(input())

for i in range(n):
    x = int(input())
    cont = 0
    for c in range(1, x+1):
        if x % c == 0:
            cont += 1
    if cont == 2:
        print("{} eh primo". format(x))

    else:
        print("{} nao eh primo".format(x))

