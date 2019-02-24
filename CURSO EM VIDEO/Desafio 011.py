largura = input('Largura da parede: ').replace(',', '.')
largura = float(largura)
altura = input(('Altura da Parede: ')).replace(',', '.')
altura = float(altura)
area = altura * largura
listros = area/2


print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(listros))