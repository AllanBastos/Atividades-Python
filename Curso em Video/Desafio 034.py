sal = float(input('Qual o salário do funcionario? R$'))
aumento = 0
if sal >= 1250.00:
    aumento = sal + sal*0.1
else:
    aumento = sal + sal*0.15
print('Quem ganhava R${:.2f} passa a ganhar R${} agora.'.format(sal, aumento))