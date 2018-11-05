cartas_paes = [int(i) for i in input().split()]
cartas_willy = [int(i) for i in input().split()]

pontos_paes = 0
pontos_willy= 0

def menor_carta_crescente(cartas):
    c = cartas[:]
    c.sort()
    for i in range(1, len(c)):
        if c[i] != c[i - 1]+1:
            return 0
    return c[0]

def menor_carta_todas_iguais(cartas):
    for i in range(1, len(cartas)):
        if cartas[i] != cartas[i - 1]:
            return 0
    return cartas[0]

def duas_menores_cartas_iguais(cartas):
    c = cartas[:]
    c.sort()
    if c[0] == c[1] and c[0] != c[2]:
        return c[0] // 2
    return 0

def duas_maiores_cartas_iguais(cartas):
    c = cartas[:]
    c.sort()
    if c[2] == c[1] and c[0] != c[2]:
        return c[2] // 2
    return 0

def soma_oito(cartas):
    if sum(cartas) == 8:
        return 8
    return 0

pontos_paes += menor_carta_crescente(cartas_paes)
pontos_paes += menor_carta_todas_iguais(cartas_paes)
pontos_paes += duas_menores_cartas_iguais(cartas_paes)
pontos_paes += duas_maiores_cartas_iguais(cartas_paes)
pontos_paes += soma_oito(cartas_paes)

pontos_willy += menor_carta_crescente(cartas_willy)
pontos_willy += menor_carta_todas_iguais(cartas_willy)
pontos_willy += duas_menores_cartas_iguais(cartas_willy)
pontos_willy += duas_maiores_cartas_iguais(cartas_willy)
pontos_willy += soma_oito(cartas_willy)

if pontos_paes == pontos_willy:
    resultado = 0
elif pontos_paes > pontos_willy:
    resultado = 1
else:
    resultado = 2

print(resultado)