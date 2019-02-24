resultado = 10 * 6
menor = 0

for l in range(5):
    n = int(input())
    cont = 10**6
    for i in range(1, n+1):
        if n % i == 0:
            cont += i
    if resultado < cont:
        resultado = cont
        menor = n
print(menor)