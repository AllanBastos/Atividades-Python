PESSOAS = 10
QUANT_HOMEN = 0
QUANT_MULHER = 0
MEDIA_SAL_H_M = 0
MAIOR_SALARIO = 0
MEDIA_SAL_HOMENS = 0
SALARIO_ANT = 0
SALARIO = 0
MEDIA_MAN = 0
SEXO = ''
for i in range(PESSOAS):
    salario = float(input())
    sexo = input()

    SALARIO += salario

    if MAIOR_SALARIO < salario:
        MAIOR_SALARIO = salario
        SEXO = sexo

    if sexo in "m":
        QUANT_HOMEN += 1
        MEDIA_MAN += salario
        MEDIA_SAL_H = MEDIA_MAN / QUANT_HOMEN
    if sexo in "f":
        QUANT_MULHER += 1
    MEDIA_SAL_H_M = SALARIO / PESSOAS

print(QUANT_HOMEN)
print(QUANT_MULHER)
print(MEDIA_SAL_H_M)
print(SEXO)
print("{:.1f}" .format(MEDIA_SAL_H))