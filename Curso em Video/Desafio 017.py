'''
cateto_op = input('Comprimento do cateto oposto: ').replace(',', '.')
cateto_op = float(cateto_op)
cateto_ad = input('Comprimento do cateto adjacente: ').replace(',', '.')
cateto_ad = float(cateto_ad)

hipotenusa = pow(pow(cateto_op, 2) + pow(cateto_ad, 2), 1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
'''
from  math import hypot
cateto_op = input('Comprimento do cateto oposto: ').replace(',', '.')
cateto_op = float(cateto_op)
cateto_ad = input('Comprimento do cateto adjacente: ').replace(',', '.')
cateto_ad = float(cateto_ad)

hipotenusa = hypot(cateto_op, cateto_ad)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))