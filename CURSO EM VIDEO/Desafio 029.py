vel_max = 80
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > vel_max:
    multa = (velocidade - 80) * 7
    print('\033[7;40;31mMULTADO!\033[m Você excedeu o limete permitido que é de 80KM/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
