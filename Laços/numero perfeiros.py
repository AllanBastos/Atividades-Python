def perfeito(n):
    soma = 0
    for i in range(1, n+1):
        if n % i == 0:
            soma += i
    if soma  == n * 2:
        return True
    return False

n = int(input())

for i in range(1, n+1):
    if perfeito(i) and i < n:
        print(i)
