from grafo import Grafo

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M',
           'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'}

paraiba = Grafo(vertices, arestas)

grafo = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
              {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K', '5': 'K-J',
               '6': 'J-G', '7': 'J-I', '8': 'I-G', '9': 'G-H', '10': 'H-F',
               '11': 'F-B', '12': 'B-G', '13': 'B-C', '14': 'C-D', '15': 'D-E',
               '16': 'D-B', '17': 'B-E'})

test1 = Grafo(["A", "B", "C"], {'1': "A-B"})
print(paraiba)

# #testando ciclo
# print(test1.ciclo())
# print(paraiba.ciclo())
# print(grafo.ciclo())
#
# #testando caminho entre dois vertices
# print(test1.caminho_entre_dois("A", "C"))
# print(paraiba.caminho_entre_dois("J", "Z"))
# print(grafo.caminho_entre_dois("A", "K"))
#
# #testando conexão
# print(paraiba.conexo())
# print(grafo.conexo())
# print(test1.conexo())

