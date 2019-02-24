VPtotal = float(input())
Declarado = float(input())
ValorReal =  float (input())
InfoMulta = str (input())

imposto =(ValorReal * 15 )/100
multa = 0.0

if ValorReal >  0.2 * VPtotal :
    print("Imposto")
    print("{:.1f}" .format(imposto))
    print(multa)

elif ValorReal > 1000000 :

    if (ValorReal >= 1000000 and InfoMulta == "sim" ) or (ValorReal < 0.50*VPtotal):
        print("Crime")
        print("{:.1f}" .format(imposto))
        print("{:.1f}" .format(imposto))

    elif Declarado  < ValorReal* 0.1:
        print("Imposto+Multa")
        print("{:.1f}" .format(imposto))
        print("{:.1f}" .format(imposto))



else:
    print ("Isento")
    print(multa)
    print(multa)
