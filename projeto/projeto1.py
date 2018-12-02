
from projeto.funcionalidades import *

import random

import pygame



# menu principal

def menu_principal():
    global TELA
    TELA
    jogando = True

    while jogando:
        pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
        texto('Bem vindo')
        iniciar_jogo()
        jogando = False

    terminar()

# loop para começar o jogo
def iniciar_jogo():
    global relogio, TELA, fonte_basica
    pygame.init()
    relogio = pygame.time.Clock()
    TELA = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
    pygame.display.set_caption('TETRIS')
    texto('TETRIS')
    while True:

        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.play(-1, 0.0)
        run()

# jogo principal



def run():
    global grade, TELA
    locked_position = {}
    grade = criar_grade(locked_position)

    mudar_peca = False

    peca_atual = pegar_forma()
    proxima_peca = pegar_forma()

    relogio = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    jogando = True
    while jogando:



        grade = criar_grade(locked_position)
        fall_time += relogio.get_rawtime()
        relogio.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            peca_atual.y += 1
            if not (posicao_valida(peca_atual, grade)) and peca_atual.y > 0:
                peca_atual.y -= 1
                mudar_peca = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == esquerda:
                    peca_atual.x -= 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x += 1

                elif event.key == direita:
                    peca_atual.x += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x -= 1

                elif event.key == rodar:
                    peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                elif event.key == rodar_contrario:
                    peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)


                elif event.key == baixo:
                    peca_atual.y += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.y -= 1

                elif event.key == descer_tudo:
                    fall_speed -= fall_speed

                elif event.key == pause1:
                    pausado()
                elif event.key == pause:
                    pausado()



        posicao_fomato = converter_formato(peca_atual)

        for i in range(len(posicao_fomato)):
            x, y = posicao_fomato[i]
            if y > -1:
                grade[y][x] = peca_atual.cor

        if mudar_peca:
            fall_speed = 0.27
            for pos in posicao_fomato:
                p = (pos[0], pos[1])
                locked_position[p] = peca_atual.cor

            peca_atual = proxima_peca
            proxima_peca = pegar_forma()
            mudar_peca = False

            remover_linhas(grade, locked_position)

        desenhar_janela(TELA, grade)
        desenha_proxima_peca(proxima_peca, TELA)
        pygame.display.update()


        if fim_de_jogo(locked_position):
            jogando = False
            textos('Gamer Over', 60, cor_vermelha, TELA, int(LARGURA_JANELA / 2) - 170, int(ALTURA_JANELA / 2) - 30, 'segoeprint')
            pygame.time.delay(2000)
            pygame.mixer.music.stop()
            TELA.fill(cor_branca)


            menu_principal()


menu_principal()
