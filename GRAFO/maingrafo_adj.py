from grafo_adj_nao_dir import Grafo
from grafo_gabriel import Grafo as G1
from grafo import Grafo as G
# g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
# #{'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('C-M')
# g_p.adicionaAresta('C-T')
# g_p.adicionaAresta('M-T')
# g_p.adicionaAresta('T-Z')
# g_p.adicionaAresta('J-C')
#
# vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
# arestas = {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P',
#            'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'}
#
# paraiba = G(vertices, arestas)

vertices1 = ['A', 'B', 'C', 'D', 'E', 'F']

# print(vertices1)

g_e = Grafo(vertices1)
g_e.adicionaAresta('A-B')
g_e.adicionaAresta('B-C')
g_e.adicionaAresta('C-D')
g_e.adicionaAresta('D-E')
g_e.adicionaAresta('E-A')
g_e.adicionaAresta('E-F')
g_e.adicionaAresta('E-C')
g_e.adicionaAresta('F-D')
g_e.adicionaAresta('F-C')
g_e.adicionaAresta('F-B')
g_e.adicionaAresta('D-B')

g_1 = G1(vertices1)
g_1.adicionaAresta('A-B')
g_1.adicionaAresta('B-C')
g_1.adicionaAresta('C-D')
g_1.adicionaAresta('D-E')
g_1.adicionaAresta('E-A')
g_1.adicionaAresta('E-F')
g_1.adicionaAresta('E-C')
g_1.adicionaAresta('F-D')
g_1.adicionaAresta('F-C')
g_1.adicionaAresta('F-B')
g_1.adicionaAresta('D-B')


print(g_1, g_e)

print(g_e.caminho_euleriano())
print(g_1.caminho_euleriano())
