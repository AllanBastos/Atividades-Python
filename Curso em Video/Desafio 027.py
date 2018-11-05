nome_completo = input('digite seu nome completo').strip()
dividido = nome_completo.split()
primeiro = dividido[0]
ultimo = dividido[len(dividido)-1]
print('primeiro: {} \nultimo: {}'. format(primeiro, ultimo))
