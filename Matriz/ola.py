def multiplicar(matrizA, matrizB):
    linhasA = len(matrizA)
    linhasB = len(matrizB)
    colunasA = len(matrizA[0])
    colunasB = len(matrizB[0])

    novaMatriz = []

    for linha in range(linhasA):
        novaMatriz.append([])
        for coluna in range(colunasB):
            novaMatriz[linha].append(0)
            for i in range(colunasA):
                novaMatriz[linha][coluna] += matrizA[linha][i] * matrizB[i][coluna]

    for i in range(len(novaMatriz)):
        for j in range(len(novaMatriz[i])):
            if j != len(novaMatriz[i]) - 1:
                print(novaMatriz[i][j], end=' ')
            else:
                print(novaMatriz[i][j])


dados = input().split()

quantidadeLinhasMatrizA = int(dados[0])
quantidadeColunasMatrizA = int(dados[1])
quantidadeLinhasMatrizB = int(dados[1])
quantidadeColunasMatrizB = int(dados[2])

matrizA = []
matrizB = []
for i in range(quantidadeLinhasMatrizA):
    matrizA.append([int(j) for j in input().split()])
for i in range(quantidadeLinhasMatrizB):
    matrizB.append([int(j) for j in input().split()])

multiplicar(matrizA, matrizB)