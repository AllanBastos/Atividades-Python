hi, mi, hf, mf = input().split()

hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)

hora = 0
minutos = 0

hora_minutos = (hf - hi) * 60 + (mf - mi)

if hora_minutos <= 0:
    hora_minutos += 1440

while hora_minutos >= 60:
    hora += 1
    hora_minutos -= 60

while hora_minutos >= 1:
    minutos += 1
    hora_minutos -= 1



print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minutos))


