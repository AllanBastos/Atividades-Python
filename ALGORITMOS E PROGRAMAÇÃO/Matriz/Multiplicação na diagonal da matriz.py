matriz_formada = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]

while True:
    multiplicador = int(input())

    if multiplicador == 0:
        break
    for i in range(0, 4):
        for k in range(0, 4):
            matriz_formada[k][i] = int(input())

    for i in range(len(matriz_formada)):
        for k in range(len(matriz_formada[i])):
            if matriz_formada[i] == matriz_formada[k]:
                matriz_formada[i][k] *= multiplicador
            print(matriz_formada[i][k], end=' ')

        print()