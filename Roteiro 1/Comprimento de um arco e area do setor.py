raio = input()
angulo = float (input())

areaT = 3.14*(raio**2)
arearA = areaT*angulo/360

comprimentoT = 2*3.14*raio
comprimentoA = comprimentoT*angulo/360

print("{:.2f}" .format(float(comprimentoA)))
print("{:.2f}" .format(float(arearA)))

