from tkinter import *

lado = 30
q_altura = 30
q_largura = 15
altura = q_altura*lado
largura = q_largura*lado

import random

PECA_1 = [[1],
          [1],
          [1],
          [1]]

PECA_2 = [[0, 1, 0],
          [1, 1, 1]]

PECA_3 = [[1, 1],
          [1, 0],
          [1, 0]]

PECA_4 = [[1, 1],
          [1, 1]]

PECA_5 = [[1, 1, 0],
          [0, 1, 1]]

# parede
P = ' # '

TABULEIRO = [[0 for i in range(9)] for j in range(8)]

gerepeca = [PECA_1, PECA_2, PECA_3, PECA_4, PECA_5]

proxima_peca = random.choice(gerepeca)


'''
class peca:

    def desce(self):


    def gira(self):


    def esquerda(self):


    def direita(self):

    
    def desce_rapido(self):
'''

class tela:
    def __init__(self):
        self.grade = [[0 for i in range(q_largura)]for j in range(q_altura)]

class Game:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, heght=altura, bg='purple')
        self.canvas.pack()
        self.p = proxima_peca
        self.nump = 5
        self.t = tela()



    def run(self):
        self.p = proxima_peca

        while True:
            self.p.desce(self.t)
            self.canvas.after(100)
            self.window.update_idletasks()
            self.window.update()


g = Game
g.run()
