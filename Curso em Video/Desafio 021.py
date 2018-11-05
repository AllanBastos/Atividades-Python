import pygame
import time
pygame.mixer.init()
pygame.init()

tempo1 = 1
tempo2 = 0.10
tempo3 = 0.05
while True:
    eai = input('O que vc quer fazer? (musica) ou (filme)')
    fazer = input('Você quer ver/ouvir um(a) {}? '. format(eai)).lower()
    if fazer != 'n' or fazer != 'não' or fazer != 'nao':
        break
if eai == 'musica':
    print('Ta legal então vamos lá')
    print('Aumentando o volume')
    pygame.mixer.music.load('mario.mp3')
    pygame.mixer.music.play()
    for i in range(1, 30):
        print('|', end='')
        if i < 10:
            time.sleep(tempo1)
        elif i < 20:
            time.sleep(tempo2)
        elif i < 30:
            time.sleep(tempo3)

    print('Volume no maximo')
    pygame.event.wait()

elif eai == 'filme':
    print('Carregando Midia')
    pygame.mixer.movie.load('friends.mp4')
    pygame.mixer.movie.play()
    pygame.event.wait()
pygame.event.wait()