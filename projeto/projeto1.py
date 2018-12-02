from projeto.funcionalidades import *
import random
import pygame



# menu principal

def menu_principal():
    global TELA
    pygame.init()
    jogando = True

    while jogando:
        TELA

        tela_inicial()
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
        run_dificil()


# nivel facil:

def run_facil():
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
        fall_speed = frequencia_peca_f()
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
                    if event.key == esquerda:                             # para a esquerda
                        peca_atual.x -= 1                                 # caso a posição não seja valida ele volta
                        if not posicao_valida(peca_atual, grade):         # imediatamente para posição anterio
                            peca_atual.x += 1

                    elif event.key == direita:                             # movimento para direita
                        peca_atual.x += 1
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.x -= 1

                    elif event.key == rodar:                                                    # movimento rotacinal
                        peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)     # para direita
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                    elif event.key == rodar_contrario:
                        peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)    # movimento rotacinal
                        if not posicao_valida(peca_atual, grade):                               # para esquerda
                            peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)


                    elif event.key == baixo:                            # se precinado o botão para baixo
                        peca_atual.y += 1                               # ele desce uma casa rapidamente
                        if not posicao_valida(peca_atual, grade):
                            peca_atual.y -= 1

                    elif event.key == descer_tudo:                      # aqui ele aumenta  a velocidade da peca
                        fall_speed -= fall_speed                        # para descer rapidamente

                    elif event.key == pause1:
                        pausado_nivel_facil()

                    elif event.key == pause:                             # jogo é pausado
                        pausado_nivel_facil()

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
                fall_speed = frequencia_peca_f()

            desenhar_janela(TELA, grade)
            desenha_proxima_peca(proxima_peca, TELA)
            desenhar_status(nivel, pontos)
            pygame.display.update()

            if fim_de_jogo(locked_position):
                jogando = False
                textos('Gamer Over', 60, cor_branca, TELA, int(LARGURA_JANELA / 2) - 170, int(ALTURA_JANELA / 2) - 30,
                       'segoeprint')
                pygame.time.delay(1000)
                pygame.mixer.music.stop()
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
                                run_facil()

# nivel normal


def run_normal():
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
    fall_speed = frequencia_peca_n(nivel)
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

            if event.type == pygame.KEYDOWN:  # Aqui ele faz o movimento da peca
                if event.key == esquerda:  # para a esquerda
                    peca_atual.x -= 1  # caso a posição não seja valida ele volta
                    if not posicao_valida(peca_atual, grade):  # imediatamente para posição anterio
                        peca_atual.x += 1

                elif event.key == direita:  # movimento para direita
                    peca_atual.x += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x -= 1

                elif event.key == rodar:  # movimento rotacinal
                    peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)  # para direita
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                elif event.key == rodar_contrario:
                    peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)  # movimento rotacinal
                    if not posicao_valida(peca_atual, grade):  # para esquerda
                        peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)


                elif event.key == baixo:  # se precinado o botão para baixo
                    peca_atual.y += 1  # ele desce uma casa rapidamente
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.y -= 1

                elif event.key == descer_tudo:  # aqui ele aumenta  a velocidade da peca
                    fall_speed -= fall_speed  # para descer rapidamente

                elif event.key == pause1:
                    pausado()

                elif event.key == pause:  # jogo é pausado
                    pausado()

                elif event.key == menu:  # apertando TAB ele volta para tela inicial
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
            fall_speed = frequencia_peca_n(nivel)

        desenhar_janela(TELA, grade)
        desenha_proxima_peca(proxima_peca, TELA)
        desenhar_status(nivel, pontos)
        pygame.display.update()

        if fim_de_jogo(locked_position):
            jogando = False
            textos('Gamer Over', 60, cor_branca, TELA, int(LARGURA_JANELA / 2) - 170, int(ALTURA_JANELA / 2) - 30,
                   'segoeprint')
            pygame.time.delay(1000)
            pygame.mixer.music.stop()
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
                                pygame.mixer.music.load('tetrisb.mid')  # comecar novo jogo
                            else:
                                pygame.mixer.music.load('tetrisc.mid')
                            pygame.mixer.music.play(-1, 0.0)
                            run_normal()


# nivel_dificil

def run_dificil():
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
    fall_speed = frequencia_peca_d(nivel)
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

            if event.type == pygame.KEYDOWN:  # Aqui ele faz o movimento da peca
                if event.key == esquerda:  # para a esquerda
                    peca_atual.x -= 1  # caso a posição não seja valida ele volta
                    if not posicao_valida(peca_atual, grade):  # imediatamente para posição anterio
                        peca_atual.x += 1

                elif event.key == direita:  # movimento para direita
                    peca_atual.x += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x -= 1

                elif event.key == rodar:  # movimento rotacinal
                    peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)  # para direita
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)

                elif event.key == rodar_contrario:
                    peca_atual.rotacao = peca_atual.rotacao - 1 % len(peca_atual.forma)  # movimento rotacinal
                    if not posicao_valida(peca_atual, grade):  # para esquerda
                        peca_atual.rotacao = peca_atual.rotacao + 1 % len(peca_atual.forma)


                elif event.key == baixo:  # se precinado o botão para baixo
                    peca_atual.y += 1  # ele desce uma casa rapidamente
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.y -= 1

                elif event.key == descer_tudo:  # aqui ele aumenta  a velocidade da peca
                    fall_speed -= fall_speed  # para descer rapidamente

                elif event.key == pause1:
                    pausado()

                elif event.key == pause:  # jogo é pausado
                    pausado()

                elif event.key == menu:  # apertando TAB ele volta para tela inicial
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
            fall_speed = frequencia_peca_d(nivel)

        desenhar_janela(TELA, grade)
        desenha_proxima_peca(proxima_peca, TELA)
        desenhar_status(nivel, pontos)
        pygame.display.update()

        if fim_de_jogo(locked_position):
            jogando = False
            textos('Gamer Over', 60, cor_branca, TELA, int(LARGURA_JANELA / 2) - 170, int(ALTURA_JANELA / 2) - 30,
                   'segoeprint')
            pygame.time.delay(1000)
            pygame.mixer.music.stop()
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
                                pygame.mixer.music.load('tetrisb.mid')  # comecar novo jogo
                            else:
                                pygame.mixer.music.load('tetrisc.mid')
                            pygame.mixer.music.play(-1, 0.0)
                            run_dificil()


menu_principal()
