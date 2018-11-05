numero = int(input("digite um numero"))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('analisando o numero {} \nunidade: {} \ndezena: {} \ncentena: {}\nmilhar: {}' .format(numero, unidade, dezena, centena , milhar))