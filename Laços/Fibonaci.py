while True:
    termo1 = 0
    termo2 = 1
    cont = 3
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(0)
    else:
        print(termo1, termo2, end=' ')
        while cont <= n:
            termo3 = termo1 + termo2
            print(termo3, end=' ')
            termo1 = termo2
            termo2 = termo3
            cont += 1
    print("\n")