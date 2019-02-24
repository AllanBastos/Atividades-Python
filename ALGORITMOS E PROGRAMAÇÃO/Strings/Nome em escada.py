nome = input().strip().upper()
cont = 1
for i in range(len(nome)+1):
    while cont < len(nome)+1:
        print(nome[:cont])
        cont += 1