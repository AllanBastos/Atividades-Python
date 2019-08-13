from grafo import Grafo

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
# arestas = {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M',
#            'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'}

paraiba = Grafo(vertices)
paraiba.adicionaAresta('a1', 'J-C')
paraiba.adicionaAresta('a2', 'C-E')

print(paraiba.ha_paralelas())