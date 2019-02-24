n = int(input())
if n >= 0:
    while True:
        print(n)
        n = int(input())
        if n < 0:
            print(n)
            break

else:
    print(n)