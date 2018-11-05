temp_C = input('Informe a temperatura em °C: ').replace(',', '.')
temp_C = float(temp_C)
temp_F = (temp_C * 9/5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(temp_C, temp_F))
