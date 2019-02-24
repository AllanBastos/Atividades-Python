matriz = []
soma_matriz = []
tam = int(input())
soma = 0
if tam == 1:
    entrada = input().split()
    print('tr(A) = (' + str(entrada[0]) + '.00' + ') = ' + str(entrada[0]) + '.00')
else:


    for i in range(tam):
        lista = [float(i) for i in input().split()]
        matriz.append(lista)
        if matriz[i][i] == matriz[i][i]:
            soma_matriz.append(matriz[i][i])
            soma += float(matriz[i][i])
    print('tr(A) = ', end='')
    for l in range(len(soma_matriz)):

        if l != (tam-1):
            print('(' + str('%.2f'%soma_matriz[l]) + ')' + ' + ', end='')
        else:
            print('(' + str('%.2f'%soma_matriz[l]) + ')', end='')
    print(' = %.2f'% soma)
