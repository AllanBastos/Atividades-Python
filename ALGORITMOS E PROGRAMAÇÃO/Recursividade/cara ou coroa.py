def cara_cora(n, d):
    diferença = 0
    if n == d:
        return 2
    if n == 0:
        return 0
    if (d == 0) :
        return n
    if n % d == 0:
        diferença += n * d
        cara_cora(n-1, d)
    return diferença

entrada = input().split()
N = int(entrada[0])
D = int(entrada[1])

print(cara_cora(N, D))
