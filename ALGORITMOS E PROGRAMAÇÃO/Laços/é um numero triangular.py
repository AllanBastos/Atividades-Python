def triangular(n):
    t = 'Falso'
    for i in range(0, n+1):
        if i * (i+1) * (i+2) == n:
            t = "Verdadeiro"
            print(i, '*', i+1, '*', i+2, '=', n )
    return t


numero = int(input())
if numero == 0:
    print('Falso')

else:
    print(triangular(numero))
