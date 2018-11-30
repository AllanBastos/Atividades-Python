
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
    fall_speed = 0.27


    sair = True
    while sair:
        fall_speed = 0.27
        grade = criar_grade(locked_position)
        fall_time += relogio.get_rawtime()
        relogio.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            peca_atual.y += 1
            if not (posicao_valida(peca_atual, grade)) and peca_atual.y > 0:
                peca_atual.y -= 1
                mudar_peca = True


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

        posicao_fomato = converter_formato(peca_atual)

        for i in range(len(posicao_fomato)):
            x, y = posicao_fomato[i]
            if y > -1:
                grade[x][y] = peca_atual.cor

        if mudar_peca:
            for pos in posicao_fomato:
                p = (pos[0], pos[1])
                locked_position[p] = peca_atual.cor

            peca_atual = proxima_peca
            proxima_peca = pegar_forma()
            mudar_peca = False

        if check_lost(locked_position):
            sair = False


        desenhar_janela(TELA, grade)



    terminar()



main()



