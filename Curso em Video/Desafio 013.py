salario = input('Qual é o Salário do Funcionario? R$').replace(',', '.')
salario = float(salario)
aumento = salario + (salario*0.15)
print('Um Funcionário que ganhava R${:.2f}, com 15% de aumento, '
      'passa a receber R${:.2f}'.format(salario, aumento))