def linha(c):
    print(c*10)
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
while True:
    jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
    if jogador not in (0 , 1, 2):
        break
    comutador = randint(0, 2)

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    linha('-=-')
    print('Computador jogou {}'.format(itens[comutador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    linha('-=-')
    if (comutador == 0 and jogador == 2) or (comutador == 1 and jogador == 0) or (comutador == 2 and jogador == 1):
        print('\033[31mCOMPUTADOR VENCE\033[m\n')
    elif comutador == jogador:
        print('\033[32mEMPATE\033[m\n')
    else:
        print('\033[35mVOCÊ VENCEU\033[m\n')
