salario = float(input())
horas = int(input())

valorDia = salario/44
valorHX = (valorDia/100)*10
valorHX2 = valorHX + valorDia
total = valorHX2 * horas
final = total + salario

print (("{:.2f}") .format(float(final)))



