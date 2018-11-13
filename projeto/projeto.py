import pygame
import random
import sys
import time
from pygame.locals import *

FPS = 25
LARGURA_JANELA = 1080
ALTURA_JANELA = 720
TAMANHO_BLOCO = 20
LARGURA_TABULEIRO = 10
ALTURA_TABULERIO = 20
EM_BRANCO = -1


freq_queda = 0.15
tem_queda = pygame.time.Clock()
freq_queda_rapida = 0.10

margemx = int((LARGURA_JANELA - LARGURA_TABULEIRO * TAMANHO_BLOCO) / 2)
parte_superior = (ALTURA_JANELA - (ALTURA_TABULERIO * TAMANHO_BLOCO) - 5)

# cores

cor_branca = (255, 255, 255)
cor_azulado = (11, 139, 244)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_amarela = (255, 255, 0)
cor_preta = (0, 0, 0)

cor_peca = [cor_azulado, cor_vermelha, cor_verde, cor_amarela]

cor_borda = cor_amarela
cor_bg = cor_preta
# pecas

PECA_S = [['.....', '.....', '..OO.', '.OO..', '.....'], ['.....', '..O..', '..OO.', '...O.', '.....']]

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



def main():
    global RELOGIO, TELA, FONTEBASICA
    pygame.init()
    RELOGIO = pygame.time.Clock()
    TELA = pygame.display.set_mode((ALTURA_JANELA, LARGURA_JANELA))
    FONTEBASICA = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('TETRIS')
    mostrar_escrita('TETRIS')

    Run()


def Run():
    #    areas do jogo
    area_jogo_pecas = pygame.Surface((800, 710))
    area_jogo_pecas.fill(cor_branca)
    area_jogo_placar = pygame.Surface((265, 710))
    area_jogo_placar.fill(cor_azulado)

    #limites area do jogo

    limite_esquerdo = pygame.Rect(0, 5, 5, 710)
    limite_direito = pygame.Rect(805, 5, 5, 710)
    limite_inferior = pygame.Rect(0, 715, 810, 5)
    limite_superior = pygame.Rect(0, 0, 810, 5)



    peca1 = pygame.Rect(x, y, 30, 90)
    peca2 = pygame.Rect(x, y, 30, 30)
    peca3 = pygame.Rect(x, y, 30, 85)
    pecas = [peca1, peca2, peca3]
    proxima_peca = random.choice(pecas)
    peca = proxima_peca




    sair = False
    while sair == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN and not peca.colliderect(limite_inferior):
                if event.key == pygame.K_LEFT and not peca.colliderect(limite_esquerdo):
                    peca.move_ip(-30, 0)
                if event.key == pygame.K_RIGHT and not peca.colliderect(limite_direito):
                    peca.move_ip(30, 0)
                if event.key == pygame.K_UP:
                    peca = pygame.Rect(peca.x, peca.y, peca.height, peca.width)


        RELOGIO.tick(FPS)
        TELA.blit(area_jogo_pecas, [5, 5])
        TELA.blit(area_jogo_placar, [810, 5])

        pygame.draw.rect(TELA, cor_amarela, limite_direito)
        pygame.draw.rect(TELA, cor_amarela, limite_esquerdo)
        pygame.draw.rect(TELA, cor_amarela, limite_superior)
        pygame.draw.rect(TELA, cor_amarela, limite_inferior)


        pygame.draw.rect(TELA, cor_vermelha, peca)

        y = 5
        if not peca.colliderect(limite_inferior):
            tem_queda.tick(15)
            peca = peca.move(0, y)
            y += 5




        if peca.colliderect(limite_inferior):
            altp, larp = peca.width, peca.height
            peca_fixa = pygame.Rect(peca.x, peca.y, altp, larp)
            pygame.draw.rect(TELA, cor_verde, peca_fixa)
            proxima_peca = random.choice(pecas)
            peca = proxima_peca



        pygame.display.update()





main()