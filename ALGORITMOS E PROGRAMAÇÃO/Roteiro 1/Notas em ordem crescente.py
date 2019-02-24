n1 = int(input())
n2 = int(input())
n3 = int(input())
if 0 <= n1 <=100 and 0 <= n2 <=100 and 0 <= n3 <=100:
    if (n1 >= n2) and (n1 >= n3) :
        if (n2 >= n3): # 3,2,1
            print(n3)
            print(n2)
            print(n1)
        else: # 2,3,1
            print(n2)
            print(n3)
            print(n1)
    elif(n2 >= n1) and (n2 >= n3):
        if (n1 >= n3): # 3, 1, 2
            print(n3)
            print(n1)
            print(n2)
        else:   # 1, 3, 2
            print(n1)
            print(n3)
            print(n2)

    elif(n3 >= n1) and (n3 >= n2):
        if (n1 >= n2): # 2, 1, 3
            print(n2)
            print(n1)
            print(n3)
        else:   # 1, 2, 3
            print(n1)
            print(n2)
            print(n3)