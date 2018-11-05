forma = str(input())
if forma == "Q":
   lado = float(input())
   areaq = lado**2
   perimetroq = (lado)*4
   print(("{:.2f}") .format(areaq))
   print (perimetroq)

elif forma == ("R"):
    alturaR = float(input())
    larguraR = float(input())
    areaR = larguraR*alturaR
    perimetroR = (larguraR*2)+(alturaR*2)
    print(("{:.2f}") .format(areaR))
    print(("{:.2f}") .format(perimetroR))
elif forma == "C":
    raio = float(input())
    areaC = 3.14*raio**2
    comprimentoC = 2*3.14*raio
    print(("{:.2f}") .format(areaC))
    print(("{:.2f}") .format(comprimentoC))
else:
    print("Nenhuma figura selecionada")
