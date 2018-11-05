num = int(input('Digite um numero em Decimal que queira converter: '))

while True:
    para = int(input('Escolha uma das bases para conversão:\n\033[32m[ 1 ] para binário\n[ 2 ] para octal\n[ 3 ] para hexadecimal\n\033[mSua opação: '))
    if para  in (1, 2, 3):
        if para == 1:
            print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]).upper())
        elif para == 2:
            print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]).upper())
        elif para == 3:
            print('{} Convertido para HEXADECIAL é igual a {}'.format(num, hex(num)[2:]).upper())
        break
    else:print('\033[31mESCOLHA UMA OPÇÃO VÁLIDA\033[m')