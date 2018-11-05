saida = " "
while True:
    entrada = input().upper()
    saida = entrada
    saida = saida.replace("3","E",)
    saida = saida.replace("4", "A")
    saida = saida.replace("1", "I")
    saida = saida.replace("5", "S")
    if saida == "SAIR" or "FIM":
        break

    print(saida)