def area(l, c):
    print(f'LARGURA (m): {l}')
    print(f'COMPRIMENTO (m): {c}')
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m²')
def palavra(txt):
    print(txt)
    print('~' * len(txt))

largura = float(input('LARGURA: '))
comprimento = float(input('ALTURA: '))

palavra(' Controle de terrenos ')
area(largura, comprimento)
