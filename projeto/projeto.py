import pygame


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
    cor_branca = (255, 255, 255)
    cor_azulado = (11, 139, 244)
    cor_verde = (0, 255, 0)
    cor_vermelha = (255, 0, 0)
    cor_amarela = (255, 255, 0)
    area_jogo_pecas = pygame.Surface((800, 710))
    area_jogo_pecas.fill(cor_branca)
    area_jogo_placar = pygame.Surface((265, 710))
    area_jogo_placar.fill(cor_azulado)

    peca = pygame.Rect(x, y, tl, ta)



    sair = False
    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN and fim_da_tela != count:
                if event.key == pygame.K_LEFT:
                    peca.move_ip(-ta, 0)
                if event.key == pygame.K_RIGHT:
                    peca.move_ip(ta, 0)
                # if event.key == pygame.K_UP:
                #     peca = pygame.transform.rotate(peca90)
        relogio.tick(29)
        tela.blit(area_jogo_pecas, [5, 5])
        tela.blit(area_jogo_placar, [810, 5])
        pygame.draw.rect(tela, cor_vermelha, peca)
        y = 5

        if count != fim_da_tela:
            tem_peca.tick(15)
            peca = peca.move(0, y)
            y += 5
            count += 5
        pygame.display.update()



    pygame.quit()



run()
