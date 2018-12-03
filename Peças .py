import random

# pecas
class peca1():
    p1 = [[1],
          [1],
          [1],
          [1]]
    p2 = [1, 1, 1, 1]

class peca2():
    p1 = [[0, 1, 0],
          [1, 1, 1]]

    p2 = [[1, 0],
          [1, 1],
          [1, 0]]

    p3 = [[0, 1],
          [1, 1],
          [0, 1]]

    p4 = [[1, 1, 1],
          [0, 1, 0]]

class peca3():
    p1 = [[1, 1],
          [1, 0],
          [1, 0]]

    p2 = [[1, 1 ,1],
          [0, 0, 1]]

    p3 = [[0, 1],
          [0, 1],
          [1, 1]]

    p4 = [[1, 0, 0],
          [1, 1, 1]]

class peca4():
    p1 = [[1, 1],
          [1, 1]]

class peca5():
    p1 = [[1, 1, 0],
          [0, 1, 1]]

    p2 = [[0, 1],
          [1, 1],
          [1, 0]]



# parede
P = ' # '

TABULEIRO = [[0 for i in range(9)] for j in range(8)]

gerepeca = [peca1, peca2, peca3, peca4, peca5]

proxima_peca = random.choice(gerepeca)

print(proxima_peca)




