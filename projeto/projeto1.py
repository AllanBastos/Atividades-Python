
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

    terminar()

def run():

    locked_position = {}
    grade = criar_grade(locked_position)

    mudar_peca = False

    peca_atual = pegar_forma()
    proxima_peca = pegar_forma()

    relogio
    fall_time = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

            if event.type == pygame.KEYDOWN:
                if pygame.key == esquerda:
                    peca_atual.x -= 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x += 1
                if pygame.key == direita:
                    peca_atual.x += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x -= 1
                if pygame.key == baixo:
                    peca_atual.y += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.y -= 1
                if pygame.key == rodar:
                    peca_atual.rotacao += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao -= 1
                if pygame.key == rodar_contrario:
                    peca_atual.rotacao -= 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.rotacao += 1

        desenhar_janela(TELA, grade)

    terminar()



main()



