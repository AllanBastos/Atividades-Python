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
TELA = pygame.display.set_mode([LARGURA_JANELA,ALTURA_JANELA])


# areas do jogo
area_jogo_pecas = pygame.Surface((800, 710))
area_jogo_placar = pygame.Surface((265, 710))




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



# # limites area do jogo
#
# limite_esquerdo = pygame.Rect(0, 5, 5, 710)
# limite_direito = pygame.Rect(805, 5, 5, 710)
# limite_inferior = pygame.Rect(0, 715, 810, 5)
# limite_superior = pygame.Rect(0, 0, 810, 5)



# formas das peças

PECA_S = [['.....', '.....', '..OO.', '.OO..', '.....'], ['.....', '..O..', '..OO.', '...O.', '.....']]

PECA_Z = [['.....', '.....', '.OO..', '..OO.', '.....'], ['.....', '..O..', '.OO..', '.O...', '.....']]

PECA_I = [['..O..', '..O..', '..O..', '..O..', '.....'], ['.....', '.....', 'OOOO.', '.....', '.....']]

PECA_O = [['.....', '.....', '.OO..', '.OO..', '.....']]

PECA_J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'],
          ['.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]

PECA_L = [['.....', '...O.',  '.OOO.', '.....', '.....'], ['.....', '..O..', '..O..', '..OO.', '.....'],
          ['.....', '.....', '.OOO.', '.O...', '.....'], ['.....', '.OO..', '..O..', '..O..', '.....']]

PECA_T = [['.....', '.....', '..O..', '.OOO.', '.....'], ['.....','..O..','..OO.','..O..','.....'],
          ['.....','.....','.OOO.', '..O..', ], ['.....','..O..', '.OO..', '..O..', '.....']]


formas = [PECA_S, PECA_Z, PECA_I, PECA_O, PECA_J, PECA_L, PECA_T]

#
# PECAS = {'S': PECA_S,
#          'Z': PECA_Z,
#          'I': PECA_I,
#          'O': PECA_O,
#          'J': PECA_J,
#          'L': PECA_L,
#          'T': PECA_T}

# for i in PECAS:
#     for j in range(len(PECAS[i])):
#         dados_formato = []
#         for x in range(5):
#             coluna = []
#             for y in range(5):
#                 if PECAS[i][j][y][x] == '.':
#                     coluna.append(EM_BRANCO)
#                 else:
#                     coluna.append(1)
#             dados_formato.append(coluna)
#         PECAS[i][j] = dados_formato



# chaves

pause = pygame.K_p
pause1 = pygame.K_PAUSE
esquerda = pygame.K_LEFT
direita = pygame.K_RIGHT
baixo = pygame.K_DOWN
rodar = pygame.K_UP
rodar_contrario = pygame.K_q
descer_tudo = pygame.K_SPACE


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
        for j in range(len(grade[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grade[i][j] = c
    return grade



def converter_formato(forma):
    posicoes = []
    formato = forma.forma[forma.rotacao % len(forma.forma)]

    for i, linhas in enumerate(formato):
        linha = list(linhas)
        for j, colunas in enumerate(linha):
            if colunas == 'O':
                posicoes.append((forma.x + j, forma.y + i))

    for i, pos in enumerate(posicoes):
        posicoes[i] = (pos[0] - 2, pos[1] - 4)

    return posicoes


def posicao_valida(forma, grade):
    posicoes_aceitas = [[(j, i) for j in range(10) if grade[i][j] == (0, 0, 0)] for i in range(20)]
    posicoes_aceitas = [j for sub in posicoes_aceitas for j in sub]

    formatado = converter_formato(forma)

    for pos in formatado:
        if pos not in posicoes_aceitas:
            if pos[1] > -1:
                return False
    return True


def fim_de_jogo(posicoes):
    for pos in posicoes:
        x, y = pos

        if y < 1:
            return True
    return False



def pegar_forma():
    global formas, cor_peca

    return peca(5, 0, random.choice(formas))

def desenha_grade(tela, linhas, coluna):
    sx = topo_esquerdo_x
    sy = topo_esquerdo_y

    for i in range(linhas):
        pygame.draw.line(tela, cor_borda, (sx, sy + i * TAMANHO_BLOCO),
                         (sx + LARGURA_TABULEIRO, sy + i * TAMANHO_BLOCO))
        for j in range(coluna):
            pygame.draw.line(tela, cor_borda, (sx + j * TAMANHO_BLOCO, sy),
                             (sx + j * TAMANHO_BLOCO, sy + ALTURA_TABULEIRO))

def remover_linhas(grade, locked):
    inc = 0

    for i in range(len(grade) - 1, -1, -1):
        linha = grade[i]
        if (0, 0, 0) not in linha:
            inc += 1

            ind = i
            for j in range(len(linha)):
                try:
                    del locked[(j, i)]
                except:
                    continue

        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newkey = (x, y + inc)
                    locked[newkey] = locked.pop(key)

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
    fonte = pygame.font.SysFont(tipo, size, bold=True)
    titulo = fonte.render(texto, 1, cor)

    surface.blit(titulo, (posicaox, posicaoy))

    pygame.display.update()


def foi_precionado():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminar()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminar()
            return event.key
    return None


def desenhar_janela(tela, grade):
    tela.fill((0, 0, 0))

    pygame.font.init()
    fonte = pygame.font.SysFont('comicsans', 60)
    rotulo = fonte.render('Tetris', 1, cor_branca)

    tela.blit(rotulo, (topo_esquerdo_x + LARGURA_TABULEIRO / 2 - (rotulo.get_width() / 2), 30))

    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pygame.draw.rect(TELA, grade[i][j], (topo_esquerdo_x + j * TAMANHO_BLOCO, topo_esquerdo_y + i*TAMANHO_BLOCO,
                                                 TAMANHO_BLOCO, TAMANHO_BLOCO), 0)


    desenha_grade(tela, 20, 10)
    pygame.draw.rect(tela, (255, 0, 0), (topo_esquerdo_x, topo_esquerdo_y, LARGURA_TABULEIRO, ALTURA_TABULEIRO), 5)


def desenha_proxima_peca(forma, tela):
    fonte = pygame.font.SysFont('comicsans',  30)
    titulo = fonte.render('Proxima Peça', 1, cor_branca)

    sx = topo_esquerdo_x + LARGURA_TABULEIRO + 50
    sy = topo_esquerdo_y + ALTURA_TABULEIRO / 2 - 100
    formato = forma.forma[forma.rotacao % len(forma.forma)]
    for i, lin in enumerate(formato):
        linha= list(lin)
        for j, col in enumerate(linha):
            if col == 'O':
                pygame.draw.rect(tela, forma.cor, (sx + j * TAMANHO_BLOCO, sy + i * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 0)

    tela.blit(titulo, (sx + 10, sy - 30))


def nivel(pontos):
    pass

def pontos(algo):
    pass

def terminar():
    pygame.quit()
    sys.exit()

def pausado():
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


