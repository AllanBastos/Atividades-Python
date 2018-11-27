import random
import pygame
import sys
from pygame.locals import *

# variaveis globais

pygame.init()
FPS = 25
LARGURA_JANELA = 1080
ALTURA_JANELA = 720
ALTURA_TABULEIRO = 800
LARGURA_TABULEIRO = 500
TAMANHO_BLOCO = 50
EM_BRANCO = -1
topo_esquerdo_x = (LARGURA_JANELA - LARGURA_TABULEIRO) // 2
topo_esquerdo_y = ALTURA_JANELA - ALTURA_TABULEIRO

# areas do jogo
area_jogo_pecas = pygame.Surface((800, 710))
area_jogo_placar = pygame.Surface((265, 710))


frequencia_movimento = 0.15
descer_freqiencia = 0.10

margemx = int((LARGURA_JANELA - LARGURA_TABULEIRO * TAMANHO_BLOCO) / 2)
parte_superior = (ALTURA_JANELA - (ALTURA_TABULEIRO * TAMANHO_BLOCO) - 5)


cor_branca = (255, 255, 255)
cor_azulado = (11, 139, 244)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_amarela = (255, 255, 0)
cor_preta = (0, 0, 0)

cor_peca = [cor_azulado, cor_vermelha, cor_verde, cor_amarela]
cor_borda = cor_amarela
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

formas = [PECA_S, PECA_Z, PECA_I, PECA_O, PECA_J, PECA_L]


PECAS = {'S': PECA_S,
         'Z': PECA_Z,
         'I': PECA_I,
         'O': PECA_O,
         'J': PECA_J,
         'L': PECA_L}

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




pygame.init()
# chaves
pause = K_p and K_PAUSE
esquerda = pygame.K_LEFT
direita = pygame.K_RIGHT
baixo = pygame.K_DOWN
rodar = pygame.K_UP
rodar_contrario = pygame.K_q
descer_tudo = pygame.K_SPACE


TELA = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
pygame.display.set_caption('TETRIS')
relogio = pygame.time.Clock()
tem_peca = pygame.time.Clock()


class peca(object):
    def __init__(self, x, y, forma):
        self.x = x
        self.y = y
        self.forma = forma
        self.cor = cor_peca[formas.index(forma)]
        self.rotacao = 0


def criar_grade(locked_pos={}):
    grade = [[(0,0,0)for x in range (40)] for x in range (50)]

    for i in range(len(grade)):
        for j in range(len(grade[i])):
            if (i, j) in locked_pos:
                c = locked_pos[(j,i)]
                grade = c
    return grade



def converter_formato():
    pass

def posicao_valida():
    pass

def check_lost():
    pass

def pegar_forma():

    return peca(5, 0, random.choice(formas))

def desenha_grade(tela, grade):
    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pygame.draw.rect(TELA, grade[i][j], (topo_esquerdo_x + j * TAMANHO_BLOCO, topo_esquerdo_y + i*TAMANHO_BLOCO,
                                                 TAMANHO_BLOCO, TAMANHO_BLOCO), 0)

    pygame.draw.rect(tela, (255, 0 ,0), (topo_esquerdo_x, topo_esquerdo_y, LARGURA_TABULEIRO, ALTURA_TABULEIRO), 4)



def texto(text):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)

    titleSurf = titleFont.render(text, True, cor_branca)

    titleRect = titleSurf.get_rect()

    titleRect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2))

    TELA.blit(titleSurf, titleRect)

    pressKeySurf = fonte_basica.render('Press a key to play.', True, cor_branca)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.center = (int(LARGURA_JANELA / 2), int(ALTURA_JANELA / 2) + 100)
    TELA.blit(pressKeySurf, pressKeyRect)

    while foi_precionado() == None:
        pygame.display.update()
        relogio.tick()


def foi_precionado():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminar()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminar()
            return event.key

def desenhar_janela(tela, grade):
    tela.fill((0, 0, 0))

    pygame.font.init()
    fonte = pygame.font.SysFont('comicsans', 60)
    rotulo = fonte.render('Tetris', 1, cor_branca)

    tela.blit(rotulo, (topo_esquerdo_x + LARGURA_TABULEIRO / 2 - (rotulo.get_width() / 2), 30))

    desenha_grade(tela, grade)

    pygame.display.update()

def terminar():
    pygame.quit()
    sys.exit()



