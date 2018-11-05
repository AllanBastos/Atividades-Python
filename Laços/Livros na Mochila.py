peso = int(input())
quant = 0
peso_maximo = peso
while peso_maximo <= 18:
    peso_maximo += peso
    quant += 1
    peso = int (input())

print (quant)