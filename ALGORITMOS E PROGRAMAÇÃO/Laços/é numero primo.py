num = 1
if num > 0:
    while True:
        num = int(input())
        if num < 0:
            break
        elif num == 1:
            print(0)
        elif num == 2:
            print(1)
        elif num % 2 == 0:
            print(0)
        else:
            print(1)