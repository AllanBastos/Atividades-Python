
negativos = 0
for i in range(5):
    a = float(input('Digite um valor:\n'))
    if a < 0:
        negativos += 1
print('Foram digitados', negativos, 'numeros negativos')