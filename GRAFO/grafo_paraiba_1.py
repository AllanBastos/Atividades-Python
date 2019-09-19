from grafo_adj_nao_dir import Grafo
from grafo import Grafo as G
g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
#{'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-M')
g_p.adicionaAresta('C-T')
g_p.adicionaAresta('M-T')
g_p.adicionaAresta('T-Z')
g_p.adicionaAresta('J-C')

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M',
           'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'}

paraiba = G(vertices, arestas)

print(g_p)
print(paraiba.arestas_sobre_vertice("M"))
print(g_p.arestas_sobre_vertice("M"))
