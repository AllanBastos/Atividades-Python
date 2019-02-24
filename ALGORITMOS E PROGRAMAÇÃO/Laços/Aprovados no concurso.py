notaPT = int(input())
notaMT = int(input())
notaReda = float(input())
aprovados = 0
if (notaPT >= 40 and notaMT >= 21 and notaReda >= 7):
    aprovados += 1
while notaPT > 0:
    notaPT = int(input())
    if notaPT < 0:
        break
    else:
        notaMT = int(input())
        notaReda = float(input())
        cont = notaPT
    if (notaPT >= 40 and notaMT >= 21 and notaReda >= 7):
        aprovados += 1

print(aprovados)