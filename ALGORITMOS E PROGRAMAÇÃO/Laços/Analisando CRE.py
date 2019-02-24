menor_CRE = 0
soma = 0
nota = 20
cont = 0
while True:
    matricular = input()
    if matricular == "999":
        break
    CRE = float(input())
    soma += CRE
    cont += 1
    if CRE < nota:
        nota = CRE
        menor_CRE = matricular
media = soma / cont

print(menor_CRE)
print("{:.2f}".format(media))
