melhor_marca = ''.capitalize()
valor_escolha = 10**6

while True:

    marca = input().upper()
    if marca == 'SAIR':
        break
    alcance_max_mm = int(input())
    nova_usada = input().upper()
    if nova_usada == "U":
        pontos_fungos = input()
        avarias = input()
        preco = float(input())




    if marca == 'NIKKOR' and preco < valor_escolha:
        melhor_marca = marca
        valor_escolha = preco

    elif marca == 'SIGMA' and preco < valor_escolha and alcance_max_mm >= 300:
        if nova_usada == 'N':
            melhor_marca = marca
            valor_escolha = preco
        elif nova_usada == 'U' and pontos_fungos == 'N' and avarias == 'N':
            melhor_marca = marca
            valor_escolha = preco