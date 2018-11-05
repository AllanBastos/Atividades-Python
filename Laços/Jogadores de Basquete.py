entrada_jog = input()

JOGADOR_M_P = ''
JOGADOR_Mm_P = ''
MENOR_PT = 0
MAIOR_PT = 0
Ptotais = 0
cont = 0
media = 0
if entrada_jog == ('sair'):

    print('Nenhum jogador foi registrado.')
else:
    pontos = int(input())
    Ptotais = pontos
    MENOR_PT = pontos
    MAIOR_PT = pontos
    cont += 1
    JOGADOR_Mm_P = entrada_jog
    JOGADOR_M_P = entrada_jog
if entrada_jog != "sair":
    while True:
        entrada_jog = input()
        if entrada_jog == "sair":
            break
        else:
            pontos = int(input())
            Ptotais += pontos
            cont += 1


            if pontos <= MENOR_PT:
                MENOR_PT = pontos
                JOGADOR_Mm_P = entrada_jog
            if pontos >= MAIOR_PT:
                MAIOR_PT = pontos
                JOGADOR_M_P = entrada_jog

    media = Ptotais/cont

    print(JOGADOR_Mm_P)
    print(JOGADOR_M_P)
    print("{:.2f}".format(media))