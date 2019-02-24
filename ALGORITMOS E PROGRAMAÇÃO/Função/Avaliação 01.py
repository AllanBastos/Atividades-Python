def eh_primo(n):
    cont = 0

    for c in range (1, n+1):
        if n % c == 0:
            cont += 1
    if cont != 2:
        return False
    return True

def msg(n):
    print('O numero {} nao eh primo.'.format(n))

x = int(input())
y = int(input())

soma = x + y

if not eh_primo(x):
    msg(x)
elif not eh_primo(y):
    msg(y)

if eh_primo(x) and eh_primo(y):
    if eh_primo(soma):
        print('A soma de {} e {} eh um primo.'.format(x, y))
    else:
        print('A soma de {} e {} nao eh um primo.'.format(x, y))
