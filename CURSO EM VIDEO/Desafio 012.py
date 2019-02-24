preco = input('Qual o preço do produto? R$ ').replace(',', '.')
preco = float(preco)
desconto = preco - (preco*0.05)

print('O produto que custava R${:.2f}, na promoção com desconto '
      'de 5% vai custar R${:.2f}'.format(preco, desconto))