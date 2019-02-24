i = []
while True:
    try:

        entrada = int(input())
        i.append(entrada)

    except EOFError:
        break

condição = True

while condição:
    if i[-1] < i[-2]:
        print(i[-2]+1)
        condição = False
