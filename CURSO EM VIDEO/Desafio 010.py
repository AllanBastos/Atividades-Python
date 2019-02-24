real = (input('Quanto dinheiro você tem na carteira? R$')).replace(',', '.')
real = float(real)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, real/3.67))