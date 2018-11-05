def func(numero, soma, cont, casa):
    if casa == 0:
        return soma
    if int(numero[cont]) % 2 == 0:
        soma += int(numero[cont]) * 2 * casa
    else:
        soma += int(numero[cont]) * 3 * casa
    return func(numero, soma, cont +1, casa-1)



while True:
    numero = (input())
    if numero == '0':
        break
    casas = len(numero)
    print(func(numero, 0, 0,casas))