distancia = float(input('Qual é a distância da viagem? '))

if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45
print('você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))
print('E o custo da viagem é de R${:.2f}'.format(custo))
