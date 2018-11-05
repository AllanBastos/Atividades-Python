QUANT_VENDAS = 1
VENDAS_CART = 0
VENDAS_AVISTA = 0
IDADE_CLIENT_JOVEM = 0
VALOR_MAIOR_COMPRA = 0
MEDIA_COMPRAS_AVISTA = 0
cont_compra = 0
media = int(0)


idade = int(input())
valor_compra = float(input())
tipo_pagmnt = input()
continuar = input()
IDADE_CLIENT_JOVEM = idade
if tipo_pagmnt == "V":
    VENDAS_AVISTA += valor_compra
elif tipo_pagmnt == "C":
    VENDAS_CART += valor_compra
if tipo_pagmnt == "V":
    MEDIA_COMPRAS_AVISTA += valor_compra
    cont_compra += 1

IDADE_CLIENT_JOVEM = idade
VALOR_MAIOR_COMPRA = valor_compra
while continuar == 'S':
    idade = int(input())
    valor_compra = float(input())
    tipo_pagmnt = input()
    QUANT_VENDAS += 1
    continuar = input()
    if tipo_pagmnt == "V":
        VENDAS_AVISTA += valor_compra
    elif tipo_pagmnt == "C":
        VENDAS_CART += valor_compra

    if IDADE_CLIENT_JOVEM > idade:
        IDADE_CLIENT_JOVEM = idade
    if VALOR_MAIOR_COMPRA < valor_compra:
        VALOR_MAIOR_COMPRA = valor_compra
    if tipo_pagmnt == "V":
        MEDIA_COMPRAS_AVISTA += valor_compra
        cont_compra += 1




print(QUANT_VENDAS)
if VENDAS_AVISTA != 0:
    print("{:.2f}" .format(VENDAS_AVISTA))
else:
    print(0)
if VENDAS_CART != 0:
    print("{:.2f}" .format(VENDAS_CART))
else:
    print(0)
print(IDADE_CLIENT_JOVEM)
print("{:.2f}" .format(VALOR_MAIOR_COMPRA))
if MEDIA_COMPRAS_AVISTA != 0:
    media = MEDIA_COMPRAS_AVISTA/cont_compra
    print("{:.2f}" .format(media))
else:
    print(media)