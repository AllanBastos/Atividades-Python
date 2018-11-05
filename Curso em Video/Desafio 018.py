import math
angulo = float(input('Digite um ângulo que você deseja: '))
angulo = math.radians(angulo)
seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))