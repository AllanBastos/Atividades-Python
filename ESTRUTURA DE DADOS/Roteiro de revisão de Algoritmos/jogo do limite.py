def modulo(x, y):
    m = x - y
    if m < 0:
        return m*(-1)
    else:
        return m

pontos_alice = 0
pontos_bob = 0
carta_alice = 0
carta_bob = 0

carta_atual = 0

N, T, L = input().split()
N, T, L = int(N), int(T), int(L)
carta_atual = T
for i in range(N-1):
    if i == 0 or i % 2 == 0:
        carta_alice = int(input())
        if modulo(carta_atual, carta_alice) <= L:
            pontos_alice += modulo(carta_atual, carta_alice)
            carta_atual = carta_alice
    else:
        carta_bob = int(input())
        if modulo(carta_atual, carta_bob) <= L:
            pontos_bob += modulo(carta_atual, carta_bob)
            carta_atual = carta_bob

print(pontos_alice, pontos_bob)