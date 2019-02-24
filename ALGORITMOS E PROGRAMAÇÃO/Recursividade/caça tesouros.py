def pontos(lista, n, m):
    p_total = 0
    for l in range(n):
        for c in range(m):
            if lista[l][l] == 'o' and lista[l][0] != '#':
                p_total += 10
    return p_total

entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])

lista = []
for i in range(N):
    linhas = input()
    primeiralista = []
    for l in range(6):
        primeiralista.append(linhas[l])
    lista.append(primeiralista)
print(pontos(lista, N, M))