print(('\033[35m='*8) + '  LOJAS SANTOS  ' + ('=\033[m'*8))

preco = float(input('Preço das compras: R$'))

while True:
    pgmt = int(input('''FORMAS DE PAGAMENTO
\033[33m[ 1 ] à vista dinherio/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m
Qual é a opção? '''))
    if pgmt in (1, 2 , 3, 4):
        if pgmt == 1:
            total = preco - (preco*0.1)
            print('Sua compra com o valor de R${:.2f} à vista no dinheiro\cheque, vai custar R${:.2f} com 10% de desconto'.format(preco, total))
        elif pgmt == 2:
            total = preco - (preco * 0.05)
            print('Sua compra com o valor de R${:.2f} à vista no cartão, vai custar R${:.2f} com 5% de desconto'.format(preco, total))
        elif pgmt == 3:
            total = preco /2
            print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(total))
            print('Sua compra vai custar R${:.2f} no final.'.format(preco))
        elif pgmt == 4:
            parc = int(input('Quantas parcelas? '))
            total = preco + preco*0.2
            div = total / parc
            print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, div))
            print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

        break
    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')
