
carne = input()

if carne != "C" and carne != "BF" and carne != "BS":
    print("Opção inválida.")
else:
    PAlho = input()
    BA = input()
    BC = input()
    QC = int(input())
    QA = int(input())



    if carne == "C" and PAlho == "S" and  BA == "S" and BC == "S":
        PreçoChurascoC = (6.40*QA) + (6.40*QC) + (1.80*QA) + (1.50*QA) + (16.00*QA) + (3.00*QC)

        print("R$: " + "{:.2f}" .format(PreçoChurascoC))

    elif carne == "C" and PAlho == "N" and  BA == "S" and BC == "S":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA) + (16.00 * QA) + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "C" and PAlho == "S" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA)  + (3.00 * QC))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "C" and PAlho == "S" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA) + (16.00 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "C" and PAlho == "N" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA)  + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "C" and PAlho == "N" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA) + (16.00 * QA))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "C" and PAlho == "N" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "C" and PAlho == "S" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((6.40 * QA) + (6.40 * QC) + (1.80 * QA) + (1.50 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BF" and PAlho == "S" and  BA == "S" and BC == "S":
        PreçoChurascoC = (8.00*QA) + (6.40*QC) + (2.70*QA) +  (16.00*QA) + (3.00*QC)

        print("R$: " + "{:.2f}" .format(PreçoChurascoC))

    elif carne == "BF" and PAlho == "N" and  BA == "S" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA) +   (16.00 * QA) + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "BF" and PAlho == "S" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA)   + (3.00 * QC))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BF" and PAlho == "S" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA)  + (16.00 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BF" and PAlho == "N" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA)  + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "BF" and PAlho == "N" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA)  + (16.00 * QA))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "BF" and PAlho == "N" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA) )
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "BF" and PAlho == "S" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.70 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BS" and PAlho == "S" and  BA == "S" and BC == "S":
        PreçoChurascoC = (8.00*QA) + (6.40*QC) + (2.25*QA) +  (16.00*QA) + (3.00*QC)

        print("R$: " + "{:.2f}" .format(PreçoChurascoC))

    elif carne == "BS" and PAlho == "N" and  BA == "S" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA) +   (16.00 * QA) + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "BS" and PAlho == "S" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA)   + (3.00 * QC))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BS" and PAlho == "S" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA)  + (16.00 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))

    elif carne == "BS" and PAlho == "N" and  BA == "N" and BC == "S":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA)  + (3.00 * QC))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "BS" and PAlho == "N" and  BA == "S" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA)  + (16.00 * QA))
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))


    elif carne == "BS" and PAlho == "N" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA) )
        porcentagem = PreçoChurascoC*0.02
        resultado = PreçoChurascoC - porcentagem

        print("R$: " + "{:.2f}".format(resultado))

    elif carne == "BS" and PAlho == "S" and  BA == "N" and BC == "N":
        PreçoChurascoC = ((8.00 * QA) + (6.40 * QC) + (2.25 * QA))

        print("R$: " + "{:.2f}".format(PreçoChurascoC))