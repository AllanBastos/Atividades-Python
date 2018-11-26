
from projeto.funcionalidades import *

import random
import time
import pygame

from pygame.locals import *


def main():
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
        pygame.mixer.music.stop()
        texto('Game Over')

def run():

    pygame.init()

    tabuleiro = criar_novo_tabuleiro()


    ultimo_tempo_queda = time.time()
    movimeno_lateral = time.time()
    ultimo_tempo = time.time()

    movendo_baixo = False
    movendo_esquerda = False
    movendo_direita = False

    score = 0
    level = calcular_nivel(score)
    freq_tempo = calcular_tempo(level)


    peca_atual = nova_peca()
    proxima_peca = nova_peca()

    while True:

        if peca_atual == None:
            peca_atual = proxima_peca
            proxima_peca = nova_peca()
            ultimo_tempo = time.time()

            if not posicao_valida(tabuleiro, peca_atual):
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()

            elif event.type == KEYUP:
                if event.type == K_p:
                    TELA.fill(cor_bg)
                    texto('PAUSE')
                    ultimo_tempo_queda = time.time()
                    movimeno_lateral = time.time()
                    ultimo_tempo = time.time()

                if event.Key == K_RIGHT:
                    movendo_direita = False
                if event.Key == K_LEFT:
                    movendo_esquerda = False
                if event.Key == K_DOWN:
                    movendo_baixo = False

            elif event.type == KEYDOWN:
                if event.Key == K_LEFT and posicao_valida(tabuleiro, peca_atual,  adjX=-1):
                    peca_atual['x'] -= 1
                    movimeno_lateral = time.time()
                    movendo_esquerda = True
                    movendo_direita = False
                    movimeno_lateral = time.time()
                if event.Key == K_RIGHT and posicao_valida(tabuleiro, peca_atual, adjX=1):
                    peca_atual['x'] += 1
                    movimeno_lateral = time.time()
                    movendo_direita = True
                    movendo_esquerda = False
                    movimeno_lateral = time.time()
                if event.Key == K_UP:
                    peca_atual['rotacao'] = (peca_atual['rotacao'] + 1) % len(PECAS[peca_atual['forma']])
                    if not posicao_valida(tabuleiro, peca_atual):
                        peca_atual['rotacao'] = (peca_atual['rotacao'] - 1) % len(PECAS[peca_atual['forma']])
                if event.Key == rodar_contrario:
                    peca_atual['rotacao'] = (peca_atual['rotacao'] - 1) % len(PECAS[peca_atual['forma']])
                    if not posicao_valida(tabuleiro, peca_atual):
                        peca_atual['rotacao'] = (peca_atual['rotacao'] + 1) % len(PECAS[peca_atual['forma']])


                if event.Key == K_DOWN:
                    movendo_baixo = True
                    if posicao_valida(tabuleiro, peca_atual, adjY=1):
                        peca_atual['y'] += 1
                    ultimo_tempo_queda = time.time()

                if event.Key == descer_tudo:
                    movendo_baixo = False
                    movendo_esquerda = False
                    movendo_direita = False
                    for i in range(1, ALTURA_TABULEIRO):
                        if not posicao_valida(tabuleiro, peca_atual, adjY=i):
                            break

                    peca_atual['y'] += (i - 1)

                if event.type == sair:
                    terminar()


        if (movendo_direita or movendo_esquerda) and time.time() - movimeno_lateral > frequencia_movimento:
            if movendo_esquerda and posicao_valida(tabuleiro, peca_atual, adjX=-1):
                peca_atual['x'] -= 1
            if movendo_direita and posicao_valida (tabuleiro, peca_atual, adjX=1):
                peca_atual['x'] += 1
            movimeno_lateral = time.time()

        if movendo_baixo and time.time() - ultimo_tempo_queda > descer_freqiencia and posicao_valida(tabuleiro, peca_atual, adjY=1):
            peca_atual['y'] += 1
            ultimo_tempo_queda = time.time()


        if time.time() - ultimo_tempo > freq_tempo:

            if atingiu_fundo(tabuleiro, peca_atual):
                add_no_tabuleiro(tabuleiro, peca_atual)
                score += deletar_linhas_completas(tabuleiro)
                level = calcular_nivel(score)
                freq_tempo = calcular_tempo(level)
                peca_atual = None

            else:
                peca_atual['y'] += 1
                movimeno_lateral = time.time()


        # TELA.blit(area_jogo_pecas, [5, 5])
        desenha_tabulerio(tabuleiro)
        desenha_borda()
        # TELA.blit(area_jogo_placar, [810, 5])
        # pygame.draw.rect(TELA, cor_amarela, limite_direito)
        # pygame.draw.rect(TELA, cor_amarela, limite_esquerdo)
        # pygame.draw.rect(TELA, cor_amarela, limite_superior)
        # pygame.draw.rect(TELA, cor_amarela, limite_inferior)

        if peca_atual != None:
            desenha_peca(peca_atual)




        pygame.display.update()
        relogio.tick(FPS)




main()



