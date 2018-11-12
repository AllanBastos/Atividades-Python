import pygame
import random

def run():
    pygame.init()
    # localização
    x = 360
    y = 5


    # tamanho


    tela = pygame.display.set_mode([1100, 740])
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



    # limite_esquerdo = pygame.Surface((5, 710))
    # limite_direito = pygame.Surface((5, 710))
    # limite_inferior = pygame.Surface((810, 5))
    # limite_superior = pygame.Surface((810, 5))

    #pecas

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


        relogio.tick(29)
        tela.blit(area_jogo_pecas, [5, 5])
        tela.blit(area_jogo_placar, [810, 5])

        pygame.draw.rect(tela, cor_amarela, limite_direito)
        pygame.draw.rect(tela, cor_amarela, limite_esquerdo)
        pygame.draw.rect(tela, cor_amarela, limite_superior)
        pygame.draw.rect(tela, cor_amarela, limite_inferior)


        pygame.draw.rect(tela, cor_vermelha, peca)

        y = 5




        if not peca.colliderect(limite_inferior):
            tem_peca.tick(15)
            peca = peca.move(0, y)
            y += 5

        altp, larp = peca.width, peca.height


        peca_fixa = pygame.Rect(peca.x, peca.y, altp, larp)

        if peca.colliderect(limite_inferior):
            peca = pygame.draw.rect(tela, cor_verde, peca_fixa)





        pygame.display.update()



    pygame.quit()



run()
