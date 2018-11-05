valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Quantos Anos pretende pagar? '))

tempo_meses = anos * 12

prestacao = valor_casa / tempo_meses
if prestacao > salario*0.3:
    print('Infelisente não podemos disponibilizar o emprestimo à você')
else:
    print('A prestação da casa por mês será de R${:.2f} durante {} meses.'.format(prestacao, tempo_meses))
