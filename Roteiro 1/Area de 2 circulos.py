raio1 = float(input())
raio2 = float(input())

circulo1= 3.14*raio1**2
circulo2 = 3.14*raio2**2

if circulo1 > circulo2:
    print("Primeiro circulo")

elif circulo1 < circulo2:
    print("Segundo circulo")

else:
    print("Iguais")