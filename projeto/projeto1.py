
from projeto.funcionalidades import *
import random
import pygame
pygame.init()



def menu_principal():
    global TELA
    pygame.init()
    pygame.mixer.music.stop()
    while True:
        fundo = pygame.image.load('tetrismenu.png')
        TELA.blit(fundo, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == K_1:
                    menu_jogar()

                elif event.key == K_2:
                    menu_raking()

                elif event.key == K_3:
                    menu_ajuda()
                elif event.key == K_4:
                    terminar()



        pygame.display.update()


def menu_jogar():
    global jogador_nivel_3, jogador_nivel_1, jogador_nivel_2
    jogador_nivel_1 = ''
    jogador_nivel_2 = ''
    jogador_nivel_3 = ''
    while True:
        fundo = pygame.image.load('menunivel.png')
        TELA.blit(fundo, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == K_1:
                    jogador_nivel_1 = input_texto(TELA)
                    iniciar_jogo(1)

                elif event.key == K_2:
                    jogador_nivel_2 = input_texto(TELA)
                    iniciar_jogo(2)

                elif event.key == K_3:
                    jogador_nivel_3 = input_texto(TELA)
                    iniciar_jogo(3)

                elif event.key == pygame.K_TAB:
                    menu_principal()
        pygame.display.update()

def menu_ajuda():
    while True:
        fundo = pygame.image.load('menuajuda.png')
        TELA.blit(fundo, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    menu_principal()
        pygame.display.update()


def menu_raking():
    print(mostrar_rankin())
    while True:
        fundo = pygame.image.load('menuranking.png')
        TELA.blit(fundo, (0, 0))
        mostrar_rankin()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    menu_principal()
        pygame.display.update()


def iniciar_jogo(modo):
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

        if modo == 1:
            run(1)

        elif modo == 2:
            run(2)

        elif modo == 3:
            run(3)




# nivel facil:

def run(modo):
        global grade, TELA


        locked_position = {}
        grade = criar_grade(locked_position)

        mudar_peca = False

        peca_atual = pegar_forma()
        proxima_peca = pegar_forma()

        relogio = pygame.time.Clock()
        fall_time = 0
        nivel = 1
        pontos = 0
        if modo == 1:
            fall_speed = frequencia_peca_f()
            ultimo_record = record_maxf()
        elif modo == 2:
            fall_speed = frequencia_peca_n(nivel)
            ultimo_record = record_maxn()
        else:
            fall_speed = frequencia_peca_d(nivel)
            ultimo_record = record_maxd()
        jogando = True
        while jogando:

            grade = criar_grade(locked_position)
            fall_time += relogio.get_rawtime()
            relogio.tick()

            if fall_time / 1000 > fall_speed:
                fall_time = 0
                peca_atual.y += 1
                if not (posicao_valida(peca_atual, grade)) and peca_atual.y > 0:
                    peca_atual.y -= 1
                    mudar_peca = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminar()

                if event.type == pygame.KEYDOWN:                          # Aqui ele faz o movimento da peca
                    if event.key == esquerda or event.key == pygame.K_a:  # para a esquerda
                        peca_atual.x -= 1                                 # caso a posição não seja valida ele volta
                        if not posicao_valida(peca_atual, grade):         # imediatamente para posição anterio
                            peca_atual.x += 1

                    elif event.key == direita or event.key == pygame.K_d:                             # movimento para direita
                        peca_atual.x += 1
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.x -= 1

                    elif event.key == rodar or event.key == pygame.K_w:                                                    # movimento rotacinal
                        peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)     # para direita
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                    elif event.key == rodar_contrario:
                        peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)    # movimento rotacinal
                        if not posicao_valida(peca_atual, grade):                               # para esquerda
                            peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)


                    elif event.key == baixo or event.key == pygame.K_s:     # se precinado o botão para baixo
                        peca_atual.y += 1                                   # ele desce uma casa rapidamente
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.y -= 1

                    elif event.key == descer_tudo:                      # aqui ele aumenta  a velocidade da peca
                        fall_speed -= fall_speed                        # para descer rapidamente



                    elif event.key == pause:                             # jogo é pausado
                        if modo == 1:
                            pausado_nivel_facil()
                        else:
                            pausado()

                    elif event.key == menu:                             # apertando TAB ele volta para tela inicial
                        menu_principal()

            posicao_fomato = converter_formato(peca_atual)

            for i in range(len(posicao_fomato)):
                x, y = posicao_fomato[i]
                if y > -1:
                    grade[y][x] = peca_atual.cor

            if mudar_peca:

                for pos in posicao_fomato:
                    p = (pos[0], pos[1])
                    locked_position[p] = peca_atual.cor

                peca_atual = proxima_peca
                proxima_peca = pegar_forma()
                mudar_peca = False

                pontos += remover_linhas(grade, locked_position) * 2
                nivel = calcular_nivel(pontos)
                if (modo == 1):
                    fall_speed = frequencia_peca_f()
                    recordf(pontos*100)
                elif (modo == 2):
                    fall_speed = frequencia_peca_n(nivel)
                    recordn(pontos*100)
                elif (modo == 3):
                    fall_speed = frequencia_peca_d(nivel)
                    recordd(pontos*100)

            if modo == 3:
                desenhar_janela_dificil(TELA, grade)
            else:
                desenhar_janela(TELA, grade)
            desenha_proxima_peca(proxima_peca, TELA)
            desenhar_status(nivel, pontos, ultimo_record)
            pygame.display.update()

            if fim_de_jogo(locked_position):
                jogando = False
                textos('Gamer Over', 60, cor_branca, TELA, int(LARGURA_JANELA / 2) - 170, int(ALTURA_JANELA / 2) - 30,
                       'VCR_OSD_MONO_1.001.ttf')
                pygame.time.delay(1000)
                pygame.mixer.music.stop()
                if modo == 1:
                    add_ranking1(jogador_nivel_1, pontos*100)
                while True:
                    TELA.fill(cor_branca)
                    listatext = ['Precione \'TAB\' para ir para ir para o menu', 'ou',
                                 'Precine \'ESPAÇO\' para jogar novamente']
                    multipos_textos(listatext, TELA)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminar()

                        if event.type == pygame.KEYDOWN:
                            if event.key == menu:
                                menu_principal()

                            elif event.key == pygame.K_SPACE:
                                if random.randint(0, 1) == 0:
                                    pygame.mixer.music.load('tetrisb.mid')   # comecar novo jogo
                                else:
                                    pygame.mixer.music.load('tetrisc.mid')
                                pygame.mixer.music.play(-1, 0.0)
                                if modo == 1:
                                    run(1)
                                elif modo == 2:
                                    run(2)
                                elif modo == 3:
                                    run(3)


menu_principal()