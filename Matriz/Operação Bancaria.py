def valor_credito(c):
    soma = 0
    for i in range(len(c)):
        c[i] = float(c[i])
        soma += c[i]
    return soma

def valor_debito(d):
    soma = 0
    for i in range(len(d)):
        d[i] = float(d[i])
        soma += d[i]
    return soma

credito = []
debito = []

while True:
    entrada = input().split()
    if entrada[0] == '-1':
        break
    if entrada[0] == '1':
        credito.append(entrada[1])
    elif entrada[0] == '0':
        debito.append(entrada[1])

print('Creditos: R$ {:.2f}'.format(valor_credito(credito)))
print('Debitos: R$ {:.2f}'.format(valor_debito(debito)))
print('Saldo: R$ {:.2f}'.format((valor_credito(credito)-valor_debito(debito))))