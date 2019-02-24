import pygame
import random
from projeto.funcionalidades import *
def desenha_peca(peca_atual):
    for i in range(len(peca_atual)):
        for j in range(len(peca_atual[i])):
            if peca_atual[j] == 'O':
                pygame.draw.rect(TELA, (peca_atual[i][j]), (0, 255, 0), 300)

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



peca_atual = random.choice(formas)

def run():
    pygame.init()
    x = 360
    y = 5
    tl = 50
    ta = 30
    count = 0
    fim_da_tela = 660 + ta - 10

    tela = pygame.display.set_mode([1080, 720])
    pygame.display.set_caption('TETRIS')

    relogio = pygame.time.Clock()
    tem_peca = pygame.time.Clock()

    # cores

    cor_branca = (255, 255, 255)
    cor_azulado = (11, 139, 244)
    cor_verde = (0, 255, 0)
    cor_vermelha = (255, 0, 0)
    cor_amarela = (255, 255, 0)

    # areas do jogo
    area_jogo_pecas = pygame.Surface((800, 710))
    area_jogo_pecas.fill(cor_branca)
    area_jogo_placar = pygame.Surface((265, 710))
    area_jogo_placar.fill(cor_azulado)

    #limites area do jogo

    limite_esquerdo = pygame.Rect(0, 5, 5, 710)
    limite_direito = pygame.Rect(805, 5, 5, 710)
    limite_inferior = pygame.Rect(0, 715, 810, 5)
    limite_superior = pygame.Rect(0, 0, 810, 5)

    #pecas

    peca1 = pygame.Rect(x, y, 90, 30)
    peca2 = pygame.Rect(x, y, 30, 30)
    peca3 = pygame.Rect(x, y, 10, 10)
    pecas = [peca1, peca2, peca3]
    proxima_peca = random.choice(pecas)
    peca = proxima_peca


    sair = False
    while sair == False:
        # if fim_da_tela == 0:
        #     peca = proxima_peca

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True



            if event.type == pygame.KEYDOWN and fim_da_tela != count:
                if event.key == pygame.K_LEFT:
                    peca.y -= 1
            if event.type == pygame.KEYDOWN and not peca.colliderect(limite_inferior):
                if event.key == pygame.K_LEFT and not peca.colliderect(limite_esquerdo):
                    peca.move_ip(-ta, 0)

                if event.key == pygame.K_RIGHT and not peca.colliderect(limite_direito):
                    peca.move_ip(ta, 0)
                # if event.key == pygame.K_UP:
                #     peca = pygame.transform.rotate(peca90)
                if event.key == pygame.K_UP:
                    peca = pygame.Rect(peca.centerx, peca.centery, peca.h, peca.w)


        relogio.tick(29)
        tela.blit(area_jogo_pecas, [5, 5])
        tela.blit(area_jogo_placar, [810, 5])

        pygame.draw.rect(tela, cor_amarela, limite_direito)
        pygame.draw.rect(tela, cor_amarela, limite_esquerdo)
        pygame.draw.rect(tela, cor_amarela, limite_superior)
        pygame.draw.rect(tela, cor_amarela, limite_inferior)

        pygame.draw.rect(tela, cor_vermelha, peca)

        y = 5

        desenha_peca(peca_atual)


        if not peca.colliderect(limite_inferior):
            tem_peca.tick(15)
            peca = peca.move(0, y)
            y += 5
            count += 5
        # else:
        #     count = 0



        # if peca.colliderect(limite_inferior):
        #     upx, upy = peca.h, peca.w
        #     peca = pygame.Surface((peca.width, peca.height))
        #     peca.fill(cor_verde)
        #     tela.blit(peca, [upx, upy])
        pygame.display.update()



    pygame.quit()



run()


