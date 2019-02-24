def linha(c):
    print(c*10)

linha('\033[33;1m-=-')
print('Analisador de Triangulos')
linha('-=-')
r1 = float(input('\033[mPrimerio segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmanto: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acimam \033[32mPODEM FORMAR\033[m um triangulo ',end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif (r1 != r2 and r2 != r3 and r1 != r3):
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acimam \033[31mNÃO PODEM FOMAR\033[m um triangulo!')


