import random

import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 25
LARGURA_JANELA = 1080
ALTURA_JANELA = 720
TAMANHO_BLOCO = 30
LARGURA_TABULEIRO = 20
ALTURA_TABULEIRO = 20
EM_BRANCO = -1

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

# areas do jogo
area_jogo_pecas = pygame.Surface((800, 710))
area_jogo_pecas.fill(cor_branca)
area_jogo_placar = pygame.Surface((265, 710))
area_jogo_placar.fill(cor_azulado)

# limites area do jogo

limite_esquerdo = pygame.Rect(0, 5, 5, 710)
limite_direito = pygame.Rect(805, 5, 5, 710)
limite_inferior = pygame.Rect(0, 715, 810, 5)
limite_superior = pygame.Rect(0, 0, 810, 5)





PECA_S = [['.....',
           '.....',
           '..OO.',
           '.OO..',
           '.....'],
          ['.....',
           '..O..',
           '..OO.',
           '...O.',
           '.....']]

PECA_Z = [['.....', '.....', '.OO..', '..OO.', '.....'], ['.....', '..O..', '.OO..', '.O...', '.....']]

PECA_I = [['..O..', '..O..', '..O..', '..O..', '.....'], ['.....', '.....', 'OOOO.', '.....', '.....']]

PECA_O = [['.....', '.....', '.OO..', '.OO..', '.....']]

PECA_J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'], ['.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]

PECA_L = [['.....', '...O.',  '.OOO.', '.....', '.....'], ['.....', '..O..', '..O..', '..OO.', '.....'], ['.....', '.....', '.OOO.', '.O...', '.....'], ['.....', '.OO..', '..O..', '..O..', '.....']]

PECAS = {'S': PECA_S,
         'Z': PECA_Z,
         'I': PECA_I,
         'O': PECA_O,
         'J': PECA_J,
         'L': PECA_L}

for i in PECAS:
    for j in range(len(PECAS[i])):
        dados_formato = []
        for x in range(5):
            coluna = []
            for y in range(5):
                if PECAS[i][j][y][x] == '.':
                    coluna.append(EM_BRANCO)
                else:
                    coluna.append(1)
            dados_formato.append(coluna)
        PECAS[i][j] = dados_formato




pygame.init()
# chaves
pause = K_p and K_PAUSE
esquerda = K_LEFT
direita = K_RIGHT
baixo = K_DOWN
rodar = K_UP
rodar_contrario = K_q
sair = K_ESCAPE
descer_tudo = K_SPACE


TELA = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
pygame.display.set_caption('TETRIS')
relogio = pygame.time.Clock()
tem_peca = pygame.time.Clock()



def calcular_nivel(pontos):
    return int(pontos / 10) + 1


def calcular_tempo(nivel):
    return 0.27 - (nivel * 0.02)


def nova_peca():
    forma = random.choice(list(PECAS.keys()))
    nova_peca = {'forma': forma,
                 'rotacao': random.randint(0, len(PECAS[forma])-1),
                 'x': int(LARGURA_JANELA /2)-2,
                 'y': -2,
                 'cor': random.randint(0, len(cor_peca)-1)}
    return nova_peca


def add_no_tabuleiro(tabuleiro, peca):
    for x in range(5):
        for y in range(5):
            if PECAS[peca['forma']][peca['rotacao']][x][y] != EM_BRANCO:
                tabuleiro[x + peca['x']][y + peca['y']] = peca['cor']


def foi_precionado():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminar()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminar()
            return event.key
    return None


def nova_borda():
    tabuleiro = []
    for i in range(LARGURA_TABULEIRO):
        tabuleiro.append([EM_BRANCO] * ALTURA_TABULEIRO)
    return tabuleiro


def atingiu_fundo(tabuleiro, peca):
    for x in range(5):
        for y in range(5):
            if PECAS[peca['forma']][peca['rotacao']][x][y] == EM_BRANCO or y + peca['y'] + 1 < 0:
                continue
            if y + peca['y'] + 1 == ALTURA_TABULEIRO:
                return True
            if tabuleiro[x + peca['x']][y + peca['y'] + 1] != EM_BRANCO:
                return True
    return False


def esta_no_tabuleiro(x, y):
    return x >= 0 and x < LARGURA_TABULEIRO and y < ALTURA_TABULEIRO


def posicao_valida(board, piece, adjX=0, adjY=0):
    for x in range(5):
        for y in range(5):
            if y + piece['y'] + adjY < 0 or PECAS[piece['forma']][piece['rotacao']][x][y] == EM_BRANCO:
                continue
            if not esta_no_tabuleiro(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != EM_BRANCO:
                return False
    return True



def linhas_completas(tabuleiro, y):
    for x in range(LARGURA_TABULEIRO):
        if tabuleiro[x][y] == EM_BRANCO:
            return False
    return True


def deletar_linhas_completas(tabuleiro):
    linhas_deletadas = 0
    y = ALTURA_TABULEIRO - 1
    while y >= 0:
        if linhas_completas(tabuleiro, y):
            # Remove the line and pull everything above it down by one line.
            linhas_deletadas += 1
            for pullDownY in range(y, 0, -1):
                for x in range(LARGURA_TABULEIRO):
                    tabuleiro[x][pullDownY] = tabuleiro[x][pullDownY - 1]
            # Set very top line to blank.
            for x in range(LARGURA_TABULEIRO):
                tabuleiro[x][0] = EM_BRANCO
        else:
            y -= 1
    return linhas_deletadas


def converter_pixels(x, y):
    return (margemx + (x * TAMANHO_BLOCO)), (parte_superior + (y * TAMANHO_BLOCO))


def desenha_borda():
    pygame.draw.rect(TELA, cor_borda,
                     (margemx - 3, parte_superior - 7, (LARGURA_TABULEIRO * TAMANHO_BLOCO) + 8, (ALTURA_TABULEIRO * TAMANHO_BLOCO) + 8), 5)


def desenha_tabulerio(board):
    # desenha_borda()
    pygame.draw.rect(TELA, cor_bg,(margemx, parte_superior, TAMANHO_BLOCO * LARGURA_TABULEIRO,  TAMANHO_BLOCO * ALTURA_TABULEIRO))

    for x in range(LARGURA_TABULEIRO):
        for y in range(ALTURA_TABULEIRO):
            if board[x][y] != EM_BRANCO:
                pixelx, pixely = converter_pixels(x, y)
                pygame.draw.rect(TELA, cor_peca[board[x][y]], (pixelx + 1, pixely + 1, TAMANHO_BLOCO - 1, TAMANHO_BLOCO - 1))




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
                    pixelx + (x * TAMANHO_BLOCO) + 1, pixely + (y * TAMANHO_BLOCO) + 1, TAMANHO_BLOCO - 1,
                    TAMANHO_BLOCO - 1))





def criar_novo_tabuleiro():
    tabuleiro = []
    for i in range(LARGURA_TABULEIRO):
        tabuleiro.append([EM_BRANCO] * ALTURA_TABULEIRO)
    return tabuleiro


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





def terminar():
    pygame.quit()
    sys.exit()




