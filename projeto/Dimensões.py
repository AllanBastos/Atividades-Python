from tkinter import *

# Dimensoes
lado = 20
q_largura = 10
q_altura = 20
largura = lado*q_largura
altura = lado*q_altura

class Peca:
    def __init__(self, x , y, tipo):
        self.x = x
        self.y = y
        #self.grade[][]
        #self.size
        if (tipo == 1):
            self.grade = [[0, 1, 0],
                          [0, 1, 1],
                          [0, 0, 1]]
            self.size = 3


    #def vira(self):


    def desce(self):
        for i in range(self.size):
            for j in range(self.size):
                if TELA.grade[self.y + 1][self.x]*self.grade[i][j] != 0:
                    return 0
        self.y += 1
        return 1

   # def direita(self):


   # def esquerda(self):


class tela:
    def __init__(self):
        self.grade = [[0 for i in range(q_largura)]for j in range(q_altura)]

    #def elimina(self):


  #  def desceLinhas(self):


 #   def desenha(self):


class Game:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, heght=altura, bg='black')
        self.canvas.pack()
        self.p = Peca(3, 1, 1)
        self.nump = 0
        self.t = tela()

  #  def gira(self, event):


   # def moveEsquerda(self, event):


    #def moveDireita(self, event):


    def desenha(self):
        for i in range(self.p.size):
            for j in range(self.p.size):
                if self.p.grade[i][j] != 0:
                    self.canvas.create_polygon([self.p.x*lado, self.p.y*lado, self.p.x*lado+lado, self.p.y*lado,self.p.x*lado+lado,
                                               self.p.y*lado+lado, self.p.x*lado, self.p.y*lado+lado], fill='green')

        #self.window.blid

    def run(self):
        self.p = Peca(3, 1, 1)

        while(True):

            self.canvas.delete('all')
            self.desenha()
            self.p.desce(self.t)



            self.canvas.after(100)
            self.window.update_idletasks()
            self.window.update()

g = Game()
g.run()

