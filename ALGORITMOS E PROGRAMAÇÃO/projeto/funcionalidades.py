
import random
import pygame
import sys
from pygame.locals import *




# variaveis globais

pygame.init()


FPS = 25
LARGURA_JANELA = 800
ALTURA_JANELA = 700
ALTURA_TABULEIRO = 600
LARGURA_TABULEIRO = 300
TAMANHO_BLOCO = 30

topo_esquerdo_x = (LARGURA_JANELA - LARGURA_TABULEIRO) // 2
topo_esquerdo_y = ALTURA_JANELA - ALTURA_TABULEIRO
TELA = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])



cor_branca = (255, 255, 255)
cor_azulado = (11, 139, 244)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_amarela = (255, 255, 0)
cor_preta = (0, 0, 0)
cor_cinza = (15, 15, 15)
cor_azul = (0, 0, 255)
cor_peca = [cor_verde, cor_azulado, cor_vermelha, cor_amarela, (255, 165, 0), cor_azul, (128, 0, 128)]
cor_borda = cor_cinza
cor_bg = cor_preta

fonte_basica = pygame.font.Font('freesansbold.ttf', 18)


# formas das peças

PECA_S = [['.....', '.....', '..OO.', '.OO..', '.....'], ['.....', '..O..', '..OO.', '...O.', '.....']]

PECA_Z = [['.....', '.....', '.OO..', '..OO.', '.....'], ['.....', '..O..', '.OO..', '.O...', '.....']]

PECA_I = [['..O..', '..O..', '..O..', '..O..', '.....'], ['.....', '.....', 'OOOO.', '.....', '.....']]

PECA_O = [['.....', '.....', '.OO..', '.OO..', '.....']]

PECA_J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'],
          ['.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]

PECA_L = [['.....', '..O..', '..O..', '..OO.', '.....'], ['.....', '.....', '.OOO.', '.O...', '.....'],
          ['.....', '.OO..', '..O..', '..O..', '.....'], ['.....', '...O.', '.OOO.', '.....', '.....']]

PECA_T = [['.....', '.....', '..O..', '.OOO.', '.....'], ['.....','..O..','..OO.','..O..','.....'],
          ['.....','.....','.OOO.', '..O..', ], ['.....','..O..', '.OO..', '..O..', '.....']]


formas = [PECA_S, PECA_Z, PECA_I, PECA_O, PECA_J, PECA_L, PECA_T]


# chaves

pause = pygame.K_p
esquerda = pygame.K_LEFT
direita = pygame.K_RIGHT
baixo = pygame.K_DOWN
rodar = pygame.K_UP
rodar_contrario = pygame.K_q
descer_tudo = pygame.K_SPACE
menu = pygame.K_TAB


pygame.display.set_caption('TETRIS')
relogio = pygame.time.Clock()


class peca(object):
    linha = 20
    coluna = 10

    def __init__(self, coluna, linha, forma):
        self.x = coluna
        self.y = linha
        self.forma = forma
        self.cor = cor_peca[formas.index(forma)]
        self.rotacao = int(0)


def criar_grade(locked_pos={}):
    grade = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grade)):
        for j in range(len(grade[i])):                          # Cria a grade do jogo
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grade[i][j] = c
    return grade


def converter_formato(forma):
    posicoes = []
    formato = forma.forma[forma.rotacao % len(forma.forma)]

    for i, linhas in enumerate(formato):
        linha = list(linhas)                                      # aqui pega o formato da peça
        for j, colunas in enumerate(linha):                       # quando nas diversas posições
            if colunas == 'O':
                posicoes.append((forma.x + j, forma.y + i))

    for i, pos in enumerate(posicoes):
        posicoes[i] = (pos[0] - 2, pos[1] - 4)

    return posicoes


def posicao_valida(forma, grade):
    posicoes_aceitas = [[(j, i) for j in range(10)
                         if grade[i][j] == (0, 0, 0)] for i in range(20)]
    posicoes_aceitas = [j for sub in posicoes_aceitas for j in sub]         # verifica se a posição é valida para
                                                                            # rotação e movimentação
    formatado = converter_formato(forma)

    for pos in formatado:
        if pos not in posicoes_aceitas:
            if pos[1] > -1:
                return False
    return True


def fim_de_jogo(posicoes):                  # aqui vai verificar se o tabuleiro na diagonal ja esta
    for pos in posicoes:                    #todo preenchido e finaliza o jogo
        x, y = pos

        if y < 1:
            return True
    return False


def pegar_forma():
    global formas, cor_peca                             # vai dizer qual vai ser a peca a vim

    return peca(5, 0, random.choice(formas))


def desenha_grade(tela, linhas, coluna):
    sx = topo_esquerdo_x                                 # desenha as grades do tabuleiro
    sy = topo_esquerdo_y

    for i in range(linhas):
        pygame.draw.line(tela, cor_borda, (sx, sy + i * TAMANHO_BLOCO),
                         (sx + LARGURA_TABULEIRO, sy + i * TAMANHO_BLOCO))
        for j in range(coluna):
            pygame.draw.line(tela, cor_borda, (sx + j * TAMANHO_BLOCO, sy),
                             (sx + j * TAMANHO_BLOCO, sy + ALTURA_TABULEIRO))


def remover_linhas(grade, locked):
    lc = 0

    for i in range(len(grade) - 1, -1, -1):
        linha = grade[i]
        if (0, 0, 0) not in linha:
            lc += 1                                              # aqui ele vai percorrer o tabuleiro
                                                                 # verificando se ja tem alguma linha
            rmv = i                                              # na horizontal completa e irar remover apenas
            for j in range(len(linha)):                          # as completas e puxar o resto para baixo se possivel
                try:
                    del locked[(j, i)]

                except:
                    continue

    if lc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < rmv:
                newkey = (x, y + lc)
                locked[newkey] = locked.pop(key)
    return lc


def texto(text):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)

    titleSurf = titleFont.render(text, True, cor_branca)

    titleRect = titleSurf.get_rect()

    titleRect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2))

    TELA.blit(titleSurf, titleRect)

    pressKeySurf = fonte_basica.render('Pressione uma tecla para começar', True, cor_branca)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2) + 100)
    TELA.blit(pressKeySurf, pressKeyRect)

    while foi_precionado() == None:
        pygame.display.update()
        relogio.tick()


def textos(texto, size, cor, surface, posicaox, posicaoy, tipo):
    pygame.font.init()
    if texto == 'Gamer Over':
        imagem = pygame.image.load('gamer over letra.png')
        TELA.blit(imagem, ( 0 , 0))
    else:
        fonte = pygame.font.SysFont(tipo, size, bold=True)
        titulo = fonte.render(texto, 1, cor)

        surface.blit(titulo, (posicaox, posicaoy))

    pygame.display.update()


def foi_precionado():                                   # se alguma tecla foi pecionada
    for event in pygame.event.get():
        if event.type == QUIT:
            terminar()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminar()
            return event.key
    return None


def desenhar_janela(tela, grade):
    image = pygame.image.load('background.png')
    tela.blit(image, (0, 0))

    pygame.font.init()
    fonte = pygame.font.SysFont('comicsans', 60)
    rotulo = fonte.render('Tetris', 1, cor_branca)

    tela.blit(rotulo, (topo_esquerdo_x + LARGURA_TABULEIRO / 2 - (rotulo.get_width() / 2), 30))

    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pygame.draw.rect(TELA, grade[i][j],
                             (topo_esquerdo_x + j * TAMANHO_BLOCO, topo_esquerdo_y + i*TAMANHO_BLOCO,
                                                 TAMANHO_BLOCO, TAMANHO_BLOCO), 0)


    desenha_grade(tela, 20, 10)
    pygame.draw.rect(tela, (255, 0, 0), (topo_esquerdo_x, topo_esquerdo_y, LARGURA_TABULEIRO, ALTURA_TABULEIRO), 5)
    pygame.display.update()

def desenhar_janela_dificil(tela, grade):
    image = pygame.image.load('background.png')
    tela.blit(image, (0, 0))

    pygame.font.init()
    fonte = pygame.font.SysFont('comicsans', 60)
    rotulo = fonte.render('Tetris', 1, cor_branca)

    tela.blit(rotulo, (topo_esquerdo_x + LARGURA_TABULEIRO / 2 - (rotulo.get_width() / 2), 30))

    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pygame.draw.rect(TELA, grade[i][j], (topo_esquerdo_x + j * TAMANHO_BLOCO, topo_esquerdo_y + i*TAMANHO_BLOCO,
                                                 TAMANHO_BLOCO, TAMANHO_BLOCO), 0)

    pygame.draw.rect(tela, (255, 0, 0), (topo_esquerdo_x, topo_esquerdo_y, LARGURA_TABULEIRO, ALTURA_TABULEIRO), 5)

    pygame.display.update()

def desenha_proxima_peca(forma, tela):

    sx = topo_esquerdo_x + LARGURA_TABULEIRO + 50
    sy = topo_esquerdo_y + ALTURA_TABULEIRO / 2 - 100
    formato = forma.forma[forma.rotacao % len(forma.forma)]
    for i, lin in enumerate(formato):
        linha= list(lin)
        for j, col in enumerate(linha):
            if col == 'O':
                pygame.draw.rect(tela, forma.cor, (sx + j * TAMANHO_BLOCO + 5, sy + i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 0)




def calcular_nivel(pontos):
    return int(pontos / 10) + 1

def frequencia_peca_n(nivel):
    return 0.27 - (nivel * 0.02)

def frequencia_peca_f():
    return 0.27

def frequencia_peca_d(nivel):
    return 0.27 - (nivel * 0.05)


def terminar():
    pygame.quit()
    sys.exit()

def pausado():                          # quando em pause a tela fica parada

    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = False



            TELA.fill(cor_bg)
            textos('Pause', 100, cor_branca, TELA, int(LARGURA_JANELA / 2) - 130, int(ALTURA_JANELA / 2) - 100, 'comicsans')
            textos('Tecle \'ESPAÇO\'  para acontinuar', 30, cor_branca, TELA, int(LARGURA_JANELA / 2) - 200, int(ALTURA_JANELA / 2) + 25, 'freesansbold.ttf')

        pygame.display.update()


def pausado_nivel_facil():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = False

            TELA.set_colorkey()
            textos('Pause', 100, cor_branca, TELA, int(LARGURA_JANELA / 2) - 130, int(ALTURA_JANELA / 2) - 100,
                   'comicsans')
            textos('Tecle \'ESPAÇO\'  para acontinuar', 30, cor_branca, TELA, int(LARGURA_JANELA / 2) - 200,
                   int(ALTURA_JANELA / 2) + 25, 'freesansbold.ttf')

        pygame.display.update()

def multipos_textos(listatext, tela):
    pygame.font.init()
    fonte = pygame.font.SysFont('segoeprint', 30, bold=True)
    texto1 = fonte.render(listatext[0], 1, cor_vermelha)
    texto2 = fonte.render(listatext[1], 1, cor_vermelha)
    texto3 = fonte.render(listatext[2], 1, cor_vermelha)

    tela.blit(texto1, (80, 180))
    tela.blit(texto2, (380, 290))
    tela.blit(texto3, (100, 400))

    textos('Precine \'ESPAÇO\' para jogar novamente', 30, cor_vermelha, TELA, int(LARGURA_JANELA / 2) - 300,int(ALTURA_JANELA / 2) + 50, 'segoeprint')

    pygame.display.update()

def desenhar_status(nivel, pontos, record=0):        # desenha o nivel a potuação e o record
        # pontos atuais
        scoreSurf = fonte_basica.render('{}' .format(pontos * 100), True, cor_branca)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (LARGURA_JANELA - 130, 55)
        TELA.blit(scoreSurf, scoreRect)

        # nivel
        levelSurf = fonte_basica.render('{}' .format(nivel), True, cor_branca)
        levelRect = levelSurf.get_rect()
        levelRect.topleft = (LARGURA_JANELA - 120, 130)
        TELA.blit(levelSurf, levelRect)

        # record
        recordSurf = fonte_basica.render('{}'.format(record), True, cor_branca)
        recordRect = recordSurf.get_rect()
        recordRect.topleft = (55, ALTURA_JANELA/2 - 50)

        TELA.blit(recordSurf, recordRect)


        pygame.display.update()

# record nivel facil
def recordf(record):
    pontos = record_maxf()
    with open('records.txt', 'w') as f:
        if int(pontos) > int(record):
            f.write((str(pontos)))
        else:
            f.write((str(record)))

def record_maxf():
    with open('records.txt', 'r') as f:
        lines = f.readlines()
        pontos = lines[0].strip()
    return pontos



#recode nivel normal
def recordn(record):
    pontos = record_maxn()
    with open('recordsn.txt', 'w') as f:
        if int(pontos) > int(record):
            f.write((str(pontos)))
        else:
            f.write((str(record)))

def record_maxn():
    with open('recordsn.txt', 'r') as f:
        lines = f.readlines()
        pontos = lines[0].strip()
    return pontos



#record nivel dificil
def recordd(record):
    pontos = record_maxd()
    with open('recordsd.txt', 'w') as f:
        if int(pontos) > int(record):
            f.write((str(pontos)))
        else:
            f.write((str(record)))

def record_maxd():
    with open('recordsd.txt', 'r') as f:
        lines = f.readlines()
        pontos = lines[0].strip()
    return pontos


def input_texto(TELA):                      # função para pegar o nome do jogador
    global relogio
    TELA
    font = pygame.font.Font(None, 32)
    relogio
    input_box = pygame.Rect(298, 338, 140, 32)
    cor_inicial = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color('dodgerblue2')
    cor = cor_inicial
    ativo = False
    texto = ''
    pronto = False

    while not pronto:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if input_box.collidepoint(event.pos):
                    ativo = not ativo
                else:
                    ativo = False

                cor = cor_ativa if ativo else cor_inicial
            if event.type == pygame.KEYDOWN:
                if ativo:
                    if event.key == pygame.K_RETURN and len(texto) > 2:
                        pronto = True
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += event.unicode
        jogador = pygame.image.load('Jogador.png')
        TELA.blit(jogador, (0, 0))
        # Render the current text.
        txt_surface = font.render(texto, True, cor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        TELA.blit(txt_surface, (301, 343))
        # Blit the input_box rect.
        pygame.draw.rect(TELA, cor_branca, input_box, 2)

        pygame.display.flip()
        relogio.tick(30)

    return texto


# mostrar o rankin de cada nivel e faz as modificações para ficar em ordem decrescente (do maior para o menor )

def add_ranking(jogador, pontos, nome):
    f = open(nome, 'a')
    f.write('%s %d \n' %(jogador, pontos))
    f.close()

def mostrar_rankin(nome1, nome2, nome3):
    aux = [nome1, nome2, nome3]
    for i in range(len(aux)):
        txt = open(aux[i], 'r')
        lista = txt.readlines()
        txt.close()
        arq = open(aux[i], 'w')
        ranking_sort(lista, arq, aux[i])
        arq.close()
    mostar()

def mostar():

    ## rankin nivel 1 ##

    f = open('ranking1.txt', 'r')
    lista = f.readlines()
    lugar1 = lista[0].split()
    lugar2 = lista[1].split()
    lugar3 = lista[2].split()
    pontos1 = lugar1.pop()
    pontos2 = lugar2.pop()
    pontos3 = lugar3.pop()

    nome1 = fonte_basica.render(str(lugar1[0]) , 1 , cor_bg)
    p1 = fonte_basica.render(str(pontos1), 1, cor_bg)
    TELA.blit(nome1, (95, 248))
    TELA.blit(p1, (515, 248))

    nome2 = fonte_basica.render(str(lugar2[0]), 1, cor_bg)
    p2 = fonte_basica.render(str(pontos2), 1, cor_bg)
    TELA.blit(nome2, (95, 272))
    TELA.blit(p2, (515, 272))

    nome3 = fonte_basica.render(str(lugar3[0]), 1, cor_bg)
    p3 = fonte_basica.render(str(pontos3), 1, cor_bg)
    TELA.blit(nome3, (95, 297))
    TELA.blit(p3, (515, 297))

   ## ranking nivel 2 ##

    g = open('ranking2.txt', 'r')
    lista = g.readlines()
    lugar1_2 = lista[0].split()
    lugar2_2 = lista[1].split()
    lugar3_2 = lista[2].split()
    pontos1_2 = lugar1_2.pop()
    pontos2_2 = lugar2_2.pop()
    pontos3_2 = lugar3_2.pop()

    nome1_2 = fonte_basica.render(str(lugar1_2[0]), 1, cor_bg)
    p1_2 = fonte_basica.render(str(pontos1_2), 1, cor_bg)
    TELA.blit(nome1_2, (95, 407))
    TELA.blit(p1_2, (515, 407))

    nome2_2 = fonte_basica.render(str(lugar2_2[0]), 1, cor_bg)
    p2_2 = fonte_basica.render(str(pontos2_2), 1, cor_bg)
    TELA.blit(nome2_2, (95, 432))
    TELA.blit(p2_2, (515, 432))

    nome3_2 = fonte_basica.render(str(lugar3_2[0]), 1, cor_bg)
    p3_2 = fonte_basica.render(str(pontos3_2), 1, cor_bg)
    TELA.blit(nome3_2, (95, 456))
    TELA.blit(p3_2, (515, 456))

    ## ranking nivel 3 ##

    h = open('ranking3.txt', 'r')
    lista = h.readlines()
    lugar1_3 = lista[0].split()
    lugar2_3 = lista[1].split()
    lugar3_3 = lista[2].split()
    pontos1_3 = lugar1_3.pop()
    pontos2_3 = lugar2_3.pop()
    pontos3_3 = lugar3_3.pop()

    nome1_3 = fonte_basica.render(str(lugar1_3[0]), 1, cor_bg)
    p1_3 = fonte_basica.render(str(pontos1_3), 1, cor_bg)
    TELA.blit(nome1_3, (95, 565))
    TELA.blit(p1_3, (515, 565))

    nome2_3 = fonte_basica.render(str(lugar2_3[0]), 1, cor_bg)
    p2_3 = fonte_basica.render(str(pontos2_3), 1, cor_bg)
    TELA.blit(nome2_3, (95, 590))
    TELA.blit(p2_3, (515, 590))

    nome3_3 = fonte_basica.render(str(lugar3_3[0]), 1, cor_bg)
    p3_3 = fonte_basica.render(str(pontos3_3), 1, cor_bg)
    TELA.blit(nome3_3, (95, 614))
    TELA.blit(p3_3, (515, 614))



def ranking_sort(lista, arquivo, nome):
    aux = []
    for n in range(len(lista)):
        var = lista[n].split()
        aux.append(int(var[len(var) - 1]))

    aux.sort()
    aux.reverse()

    while len(lista) != 0:
        for n in range(len(lista)):
            auxiliar = lista[n].split()
            valor = auxiliar[len(auxiliar) - 1]
            if aux[0] == int(valor):
                arquivo.write(lista[n])
                break
        aux.remove(aux[0])
        lista.remove(lista[n])

    f = open(nome, 'w+')
    f.write(str(aux))
    f.close()

