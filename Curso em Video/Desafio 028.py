def linha(c):
    print(c*20)
import random
import time
escolido = random.randint(0, 5)

linha('\033[1;33m-=-')
print('\033[1;32mVou pensar em um número entre 0 e 5. Tente adivinhar...')
linha('\033[1;33m-=-\033[m')

n = int(input('Em que numero eu pensei? '))
print('\033[33mPROCESSANDO...')
time.sleep(2)
if n == escolido:
    print('\032[1;32mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI!\033[m Eu pensei no número {} e não no {}!'.format(escolido, n))