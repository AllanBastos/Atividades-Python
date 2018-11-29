def multiplicar (entrada):
    '''
    A2B3
    :param entrada:
    :return:
    '''
    aux = ''
    fator = ''
    lista = []
    for n in range (len(entrada)):
        if entrada[n].isnumeric():
            fator+= entrada[n]
        else:
            lista.append(fator)
            aux+= entrada[n]
            fator = ''
        if n == len(entrada) - 1:
            lista.append(fator)
    lista.pop(0)
    fim = ''
    for n in range (len(aux)):
        fim += aux[n]* int(lista[n])

    print(fim)

vezes = int(input())

for n in range (vezes):
    entrada = input()
    multiplicar (entrada)
