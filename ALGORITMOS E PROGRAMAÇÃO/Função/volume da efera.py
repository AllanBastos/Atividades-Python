def volume_esfera(v):
    raio = (4*3.1416*v**3)/3
    return raio
for i in range(3):
    v = float(input())
    print('{:.2f}'.format(volume_esfera(v)))
