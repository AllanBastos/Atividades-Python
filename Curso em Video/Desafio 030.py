n = int(input('\033[35mMe diga um numero qualquer: \033[m'))
if n % 2 == 0:
    print('O número {} é \033[36mPAR \033[m'.format(n))
else:
    print('O número {} é \033[36mÌMPAR\033[m'.format(n))
