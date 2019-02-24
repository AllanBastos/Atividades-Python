def multiplicar(Matrix_A, Matrix_B):
    linhasA = len(Matrix_A)
    linhasB = len(Matrix_B)
    ColuasA = len(Matrix_A[0])
    ColunasB = len(Matrix_B[0])

    Matrix_C = []

    for linha in range(linhasA):
        Matrix_C.append([])
        for coluna in range(ColunasB):
            Matrix_C[linha].append(0)
            for t in range(ColuasA):
                Matrix_C[linha][coluna] += (Matrix_A[linha][t] * Matrix_B[t][coluna])

    for i in range(len(Matrix_C)):
        for j in range(len(Matrix_C[i])):
            if j != len(Matrix_C[i]) - 1:
                print(Matrix_C[i][j], end=' ')
            else:
                print(Matrix_C[i][j])


tamanhos = input().split()
Linhas_A = int(tamanhos[0])
Coluas_A_Linhas_B = int(tamanhos[1])
Colunas_B = int(tamanhos[2])
Matrix_A = []
Matrix_B = []

for i in range(Linhas_A):
    Matrix_A.append([int(j) for j in input().split()])
for i in range(Coluas_A_Linhas_B):
    Matrix_B.append([int(j) for j in input().split()])

multiplicar(Matrix_A, Matrix_B)
