

def main():
    global RELOGIO, TELA, FONTEBASICA
    pygame.init()
    RELOGIO = pygame.time.Clock()
    TELA = pygame.display.set_mode((ALTURA_JANELA, LARGURA_JANELA))
    FONTEBASICA = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('TETRIS')
    mostrar_escrita('TETRIS')
    Run()

def mostrar_escrita(texto):


    fonte_titulo = pygame.font.Font('freesansbold.ttf', 100)

    fonte_tela = fonte_titulo.render(texto, True, cor_branca)

    titulo_rect = fonte_tela.get_rect()

    titulo_rect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2))

    TELA.blit(fonte_tela, titulo_rect)

    precBotaoTela = FONTEBASICA.render('Precione um botão para começar.', True, cor_branca)
    pressKeyRect = precBotaoTela.get_rect()
    pressKeyRect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2) + 100)
    TELA.blit(precBotaoTela, pressKeyRect)

    while precionando_botao() == None:
        pygame.display.update()
        RELOGIO.tick()

def terminando():
    pygame.quit()
    sys.exit()

def Run1():

    tabuleiro = novo_tabuleiro()


    ultimadecida = time.time()
    ultimo_mov_baixo = time.time()
    ultimo_tempo_queda = time.time()

    peca1 = pygame.Rect(x, y, 50, 110)
    peca2 = pygame.Rect(x, y, 50, 50)
    peca3 = pygame.Rect(x, y, 50, 105)
    pecas = [peca1, peca2, peca3]
    proxima_peca = random.choice(pecas)
    peca = proxima_peca

    movendo_baixo = False
    movendo_esquerda = False
    movendo_direita = False

    pontos = 0
    nivel = calcular_nivel(pontos)
    queda_freq = cal_freq_queda(nivel)

    peca_atual = nova_peca()
    proxima_peca = nova_peca()

    while True:
        if peca_atual == None:
            peca_atual = proxima_peca
            proxima_peca = nova_peca()
            ultimo_tempo_queda = time.time()

            if not posicao_valida(tabuleiro, peca_atual):
                break
        for event in pygame.event.get():

            if event.type == QUIT:
                terminando()

            elif event.type == KEYUP:
                if (event.Key == K_p):
                    TELA.fill(cor_bg)

                    mostrar_escrita('Pausado')

                    ultimadecida = time.time()
                    ultimo_mov_baixo = time.time()
                    ultimo_tempo_queda = time.time()

                if event.key == K_LEFT:
                    movendo_esquerda = False
                if event.key == K_RIGHT:
                    movendo_direita = False

            elif event.type == KEYDOWN:
                # (Movendo o bloco para os lados)
                if (event.key == K_LEFT or event.key == K_a) and posicao_valida(tabuleiro, peca_atual, adjX=-1):
                    peca_atual['x'] -= 1
                    ultimo_mov_baixo = time.time()
                    movendo_esquerda = True
                    movendo_direita = False
                    ultimo_mov_baixo = time.time()
                if (event.key == K_RIGHT or event.key == K_d) and posicao_valida(tabuleiro, peca_atual, adjX=1):
                    peca_atual['x'] += 1
                    movendo_direita = True
                    movendo_esquerda = False
                    ultimo_mov_baixo = time.time()

                if (event.key == K_UP):
                    peca_atual['rotacao'] = (peca_atual['rotacao'] + 1) % len(PECAS[peca_atual['forma']])
                    if not posicao_valida(tabuleiro, peca_atual):
                        peca_atual['rotacao'] = (peca_atual['rotacao'] - 1) % len(PECAS[peca_atual['forma']])
                if event.key == pygame.K_DOWN:
                    movendo_baixo = True
                    if posicao_valida(tabuleiro, peca_atual, adjY=1):
                        peca_atual['y'] += 1
                    ultimo_mov_baixo = time.time()

                if event.key == K_SPACE:

                    movendo_baixo = False
                    movendo_esquerda = False
                    movendo_direita = False
                    for i in range(1, ALTURA_JANELA):
                        if not posicao_valida(tabuleiro, peca_atual, adjY=i):
                            break
                        peca_atual['y'] += (i - 1)
                if event.key == K_ESCAPE:
                    terminando()
        if movendo_esquerda or movendo_direita and time.time() - movendo_baixo > queda_freq:
            if movendo_esquerda and posicao_valida(tabuleiro, peca_atual, adjX=-1):
                peca_atual['x'] -= 1
            if movendo_direita and posicao_valida(tabuleiro, peca_atual, adjX=1):
                peca_atual['x'] += 1
            ultimo_mov_baixo = time.time()

        if movendo_baixo and time.time() - ultimadecida > freq_queda_rapida and posicao_valida(tabuleiro, peca_atual, adjY=1):
            peca_atual['y'] += 1
        ultimadecida = time.time()

        if time.time() - ultimo_tempo_queda > queda_freq:
            if atigiu_fundo(tabuleiro, peca_atual):

                add_tabuleiro(tabuleiro, peca_atual)
                pontos += deletar_linha_completa(tabuleiro)
                nivel = calcular_nivel(pontos)
                queda_freq = cal_freq_queda(nivel)
                peca_atual = None
            else:
                peca_atual['y'] += 1
                ultimo_tempo_queda = time.time()

        TELA.fill(cor_bg)
        desenha_tabulerio(tabuleiro)
        desenha_status(pontos, nivel)
        desenha_proximaP(proxima_peca)

        if peca_atual != None:
            desenha_peca(peca_atual)
        pygame.display.update()
        RELOGIO.tick(FPS)




            if event.type == pygame.KEYDOWN and not peca.colliderect(limite_inferior):
                if event.key == pygame.K_LEFT and not peca.colliderect(limite_esquerdo):
                    peca.move_ip(-30, 0)
                if event.key == pygame.K_RIGHT and not peca.colliderect(limite_direito):
                    peca.move_ip(30, 0)
                if event.key == pygame.K_UP:
                    peca = pygame.Rect(peca.x, peca.y, peca.height, peca.width)
                if event.key == pygame.K_DOWN:
                    tem_peca.tick(50)


def calcular_nivel(pontos):
    return int(pontos/10) + 1

def cal_freq_queda(nivel):
    return 0.27 - (nivel *0.2)

def nova_peca():
    forma = random.choice(list(PECAS.keys()))
    nova_peca = {'forma': forma,
                 'rotacao': random.randint(0, len(PECAS[forma])-1),
                 'x': int(LARGURA_JANELA /2 )-2,
                 'y': -2,
                 'cor': random.randint(0, len(cor_peca)-1) }
    return nova_peca

def add_tabuleiro(tabuleriro, peca):
    for x in range(5):
        for y in range(5):
            if PECAS[peca['forma']][peca['rotacao']][x][y] != EM_BRANCO:
                tabuleriro[x + peca['x']][y + peca['y']] = peca['cor']

def precionando_botao():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminando()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminando()
            return event.key
    return None


def novo_tabuleiro():
    tabulerio = []
    for i in range(LARGURA_JANELA):
        tabulerio.append([EM_BRANCO] * ALTURA_TABULERIO)
    return tabulerio


def atigiu_fundo(tabuleiro, peca):
    for x in range(5):
        for y in range(5):
            if PECAS[peca['forma']][peca['rotacao']][x][y] == EM_BRANCO or y + peca['y'] + 1 < 0:
                continue
            if y + peca['y'] + 1 == ALTURA_TABULERIO:
                return True
            if tabuleiro[x + peca['x']][y + peca['y'] + 1] != EM_BRANCO:
                return True
    return False

<<<<<<< Updated upstream
=======
        if not peca.colliderect(limite_inferior):
            tem_peca.tick(15)
            peca = peca.move(0, y)
            y += 10
>>>>>>> Stashed changes

def esta_no_jogo(x, y):
    return x >= 0 and x < LARGURA_JANELA and y < ALTURA_JANELA


def posicao_valida(tabuleiro, peca, adjX=0, adjY=0):
    for x in range(5):
        for y in range(5):
            if y + peca['y'] + adjY < 0 or PECAS[peca['forma']][peca['rotacao']][x][y] == EM_BRANCO:
                continue
            if not esta_no_jogo(x + peca['x'] + adjX, y + peca['y'] + adjY):
                return False
            if tabuleiro[x + peca['x'] + adjX][y + peca['y'] + adjY] != EM_BRANCO:
                return False
    return True

def linha_esta_completa(tabulerio, y):
    for x in range(LARGURA_TABULEIRO):
        if tabulerio[x][y] == EM_BRANCO:
            return False
    return True


def deletar_linha_completa(tabulerio):
    linhas_deletadas = 0
    y = ALTURA_TABULERIO - 1
    while y >= 0:
        if linha_esta_completa(tabulerio, y):

            linhas_deletadas += 1
            for pullDownY in range(y, 0, -1):
                for x in range(LARGURA_TABULEIRO):
                    tabulerio[x][pullDownY] = tabulerio[x][pullDownY - 1]
                    # Set very top line to blank.
            for x in range(LARGURA_TABULEIRO):
                tabulerio[x][0] = EM_BRANCO
        else:
            y -= 1
    return linhas_deletadas


def converter_pixels(x, y):
    return (margemx  + (x * TAMANHO_BLOCO)), (parte_superior + (y * TAMANHO_BLOCO))


def desenhar_borda_tabulerio():
    pygame.draw.rect(TELA, cor_borda,
                     (margemx - 3, parte_superior - 7, (LARGURA_TABULEIRO * TAMANHO_BLOCO) + 8, (ALTURA_TABULERIO * TAMANHO_BLOCO) + 8), 5)






def desenha_status(score, level):
    scoreSurf = FONTEBASICA.render('Score: %s' % score, True, cor_branca)
    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (LARGURA_JANELA - 150, 20)
    TELA.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = FONTEBASICA.render('Level: %s' % level, True, cor_branca)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (LARGURA_JANELA - 150, 50)
    TELA.blit(levelSurf, levelRect)



def desenha_proximaP(piece):
    nextSurf = FONTEBASICA.render('Next:', True, cor_branca)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (LARGURA_JANELA - 120, 80)
    TELA.blit(nextSurf, nextRect)

    desenha_peca(piece, customCoords=(LARGURA_JANELA - 120, 100))



def desenha_peca(piece, customCoords=(None, None)):
    shapeToDraw = PECAS[piece['forma']][piece['rotacao']]
    if customCoords == (None, None):

        pixelx, pixely = converter_pixels(piece['x'], piece['y'])
    else:
        pixelx, pixely = customCoords

        # draw each of the blocks that make up the piece
    for x in range(5):
        for y in range(5):
            if shapeToDraw[x][y] != EM_BRANCO:
                pygame.draw.rect(TELA, cor_peca[piece['cor']], (
                pixelx + (x * TAMANHO_BLOCO) + 1, pixely + (y * TAMANHO_BLOCO) + 1, TAMANHO_BLOCO - 1, TAMANHO_BLOCO - 1))
