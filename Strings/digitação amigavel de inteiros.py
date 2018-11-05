while True:
    entrada = input().upper()
    tamanho = len(entrada)
    if entrada == "FIM":
        break
    saida = entrada
    saida = saida.replace("L","1",)
    saida = saida.replace("O", "0")

    if saida.isnumeric():
        print(saida.lstrip('0'))
    else:
        print('ERRO')
