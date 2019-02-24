n = int(input())
cont = 0
while cont < n:
    pa, pb, g1, g2 = input().split()

    pa, pb, g1, g2 = int(pa), int(pb), float(g1), float(g2)

    anos = 0
    while pa <= pb:
        pa += int((pa*g1)/100)
        pb += int((pb*g2)/100)

        anos += 1

        if anos > 100:
            anos = 101
            break

    if anos == 101:
        print("Mais de 1 seculo.")

    elif anos <= 100:
        print("{} anos.".format(anos))
    cont += 1