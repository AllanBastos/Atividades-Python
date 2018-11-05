quant=int(input())
lista = ''
for i in range(quant):
    entrada = input()
    lista = entrada
    if len(lista) == 1:
        print(lista)
    if lista[0] == lista[1] or lista[-1] == lista[-2]:
        if lista[0] == lista[1]:
            Pletra = lista[0]
            lista = lista.replace(lista[0], "")
            lista = Pletra+lista

        if lista[-1] == lista[-2]:
            Uletra = lista[-1]
            lista = lista.replace(lista[-1], "").strip()
            lista = lista+Uletra
        print(lista.strip())
    else:
        print(entrada.lower())
