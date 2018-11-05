peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))

imc = peso/(altura**2)
cat = ''

if imc < 18.5:
    cat = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    cat = 'com PESO IDEAL'
elif 25 <= imc < 30:
    cat = 'com SOBREPESO'
elif 30 <= imc < 40:
    cat = 'com OBESIDADE'
elif imc >= 40:
    cat = 'com OBESIDADE MÓRBIDA'

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
print('Você está {}'.format(cat))