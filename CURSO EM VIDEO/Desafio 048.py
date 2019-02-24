# soma = 0
# quant = 0
# for n in range(1, 501, 2):
#     if n % 3 == 0:
#         soma += n
#         quant += 1
# print('A soma de todos os {} valores solicitados é {}.'.format(quant, soma))


soma = 0
quant = 0
for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        quant += 1
print('A soma de todos os {} valores solicitados é {}.'.format(quant, soma))
