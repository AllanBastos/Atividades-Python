soma = 0
cont = 0
for c in range(6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} numeros pares e a soma deles é {}'.format(cont, soma))