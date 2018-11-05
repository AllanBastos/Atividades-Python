def linha(c):
    print(c*20)


numero = int(input('Digite um número para ver sua tabuada: '))
linha("-")
for i in range(1,11):
    print('{} x {} = {}'.format(numero, i, numero*i))
linha('-')
