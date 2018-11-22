import pygame
import random
import time
from projeto.funcionalidades import *




# localização decida de peca
x = 360
y = 5

ALTURA_JANELA = 720
LARGURA_JANELA = 1080
TELA = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
pygame.display.set_caption('TETRIS')
EM_BRANCO = -1
relogio = pygame.time.Clock()
tem_peca = pygame.time.Clock()
TAMANHO_BLOCO = 50
LARGURA_TABULEIRO = 800
ALTURA_TABULEIRO = 710


margemx = int((LARGURA_JANELA - LARGURA_TABULEIRO * TAMANHO_BLOCO) / 2)
parte_superior = (ALTURA_JANELA - (ALTURA_TABULEIRO * TAMANHO_BLOCO) - 5)


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



def nova_peca():
    forma = random.choice(list(PECAS.keys()))
    nova_peca = {'forma': forma,
                 'rotacao': random.randint(0, len(PECAS[forma])-1),
                 'x': int(LARGURA_JANELA /2 )-2,
                 'y': -2,
                 'cor': random.randint(0, len(cor_peca)-1)}
    return nova_peca

peca_atual = nova_peca()
proxima_peca = nova_peca()

def atingiu_fundo(peca):
    altp, larp = peca.width, peca.height

    peca_fixa = pygame.Rect(peca.x, peca.y, altp, larp)

    return pygame.draw.rect(TELA, cor_verde, peca_fixa)


def converter_pixels(x, y):
    return (margemx  + (x * TAMANHO_BLOCO)), (710 + (y * TAMANHO_BLOCO))



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

def desenha_tabulerio(board):
    pygame.draw.rect(TELA, cor_bg, (margemx, parte_superior, TAMANHO_BLOCO * LARGURA_TABULEIRO, TAMANHO_BLOCO * ALTURA_TABULEIRO))
    for x in range(LARGURA_TABULEIRO):
        for y in range(ALTURA_TABULEIRO):
            if board[x][y] != EM_BRANCO:
                pixelx, pixely = converter_pixels(x, y)
                pygame.draw.rect(TELA, cor_peca[board[x][y]], (pixelx + 1, pixely + 1, TAMANHO_BLOCO - 1, TAMANHO_BLOCO - 1))


def run():
    global peca_atual, proxima_peca
    pygame.init()


    # tamanho




    sair = False
    while sair == False:

        if peca_atual == None:
            peca_atual = proxima_peca
            proxima_peca = nova_peca()
            #ultimo_tempo_queda = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            # if event.type == pygame.KEYDOWN :
                # if event.key == pygame.K_LEFT:
                #     peca_atual.move_ip(-30, 0)
                # if event.key == pygame.K_RIGHT:
                #     peca_atual.move_ip(30, 0)
                # if event.key == pygame.K_UP:
                #     peca_atual = pygame.Rect(peca_atual.x, peca_atual.y, peca_atual.height, peca_atual.width)


        relogio.tick(29)
        TELA.blit(area_jogo_pecas, [5, 5])
        TELA.blit(area_jogo_placar, [810, 5])

        pygame.draw.rect(TELA, cor_amarela, limite_direito)
        pygame.draw.rect(TELA, cor_amarela, limite_esquerdo)
        pygame.draw.rect(TELA, cor_amarela, limite_superior)
        pygame.draw.rect(TELA, cor_amarela, limite_inferior)


        # pygame.draw.rect(tela, cor_vermelha, peca_atual)
        if peca_atual != None:
            desenha_peca(peca_atual)
            peca_atual['y'] += 1





        #
        # if atingiu_fundo():
        #     atingiu_fundo(peca_atual)
        #     peca_atual = None




        pygame.display.update()



    pygame.quit()



run()
