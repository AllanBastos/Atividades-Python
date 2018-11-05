def matriz_imprimida(m):
    for i in range(linhas):
        for k in range(colunas):
            if k == len(m[i]) -1:
                print(m[i][k], end='\n')
            else:
                print(m[i][k], end=' ')


def soma_DP(m):
    soma = 0
    for i in range(linhas):
        for k in range(colunas):
            if m[i] == m[k]:
                soma += m[i][k]
    return soma

def soma_DS(m):
    soma = 0
    for i in range(linhas):
        for k in range(colunas):
            if i + k == len(m[i])-1 :
                soma += m[i][k]
    return soma


linhas, colunas = input().split()
linhas = int(linhas)
colunas = int(colunas)

matriz_fomarda = []
menor0 = 0
maior0 = 0
for i in range(linhas):
    matriz_fomarda.append([])
    for k in range(colunas):
        n = int(input())
        if n > 0:
            maior0 += 1
        elif n < 0:
            menor0 += 1
        matriz_fomarda[i].append(n)

print('Matriz formada:')
matriz_imprimida(matriz_fomarda)
if linhas == colunas:
    print('A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.'
      .format(soma_DP(matriz_fomarda),soma_DS(matriz_fomarda) ))
else:
    print('A diagonal principal e secundaria nao pode ser obtida.')
print('A matriz possui {} numero(s) menor(es) que zero.'
      .format(menor0))
print('A matriz possui {} numero(s) maior(es) que zero.'
      .format(maior0))