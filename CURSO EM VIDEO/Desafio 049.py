n = int(input('Digite um numero pra você ver sua tabuada: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, i*n))
