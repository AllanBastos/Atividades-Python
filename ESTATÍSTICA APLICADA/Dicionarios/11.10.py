
dicionario = dict()


with open('arquivo.txt', 'r') as a:
    linhas = a.read().split()

for i in range(len(linhas)):
    dicionario[linhas[i]] = 0

print(dicionario)

