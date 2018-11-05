x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("Primeiro Quadrante")

elif x > 0 and y < 0:
    print("Quarto Quadrante")

elif x < 0 and y > 0:
    print("Segundo Quadrante")

elif x > 0 and y > 0:
    print("Primeiro Quadrante")

elif x < 0 and y < 0:
    print("Terceiro Quadrante")

elif x == 0 and y > 0:
    print("Sobre o eixo y")

elif x == 0 and y < 0:
    print("Sobre o eixo y")

elif x < 0 and y == 0:
    print ("Sobre o eixo x")

elif x > 0 and y == 0:
    print("Sobre o eixo x")

elif x == 0 and y == 0:
    print ("Sobre a origem")
