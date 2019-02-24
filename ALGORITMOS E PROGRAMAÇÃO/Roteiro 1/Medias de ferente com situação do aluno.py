tipo = str(input())

if tipo == ("a"):
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    if 1 <= nota1 <=100 and 1 <= nota2 <=100 and 1 <= nota3 <=100:
        media = (nota1+nota2+nota3)/3
        if  70 <= media <= 100:
            print(("{:.2f}").format(media))
            print("Aprovado")

        elif 0 <= media <= 40:
            print(("{:.2f}").format(media))
            print ("Reprovado")

        elif 40 <= media <= 70:
            print(("{:.2f}").format(media))
            print ("Final")

elif tipo == ("p"):
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    pesoN1 = int(input())
    pesoN2 = int(input())
    pesoN3 = int(input())

    if 1 <= nota1 <=100 and 1 <= nota2 <=100 and 1 <= nota3 <=100 and 1 <= pesoN1 <=100 and 1 <= pesoN2 <=100 and 1 <= pesoN3 <=100:

        calculoPN = (pesoN1 * nota1 + pesoN2 * nota2 + pesoN3 * nota3)

        calculoP = (pesoN1 + pesoN2 + pesoN3)

        mediap = calculoPN/calculoP

        if 70 <= mediap <= 100:
            print(("{:.2f}").format(mediap))
            print ("Aprovado")

        elif 0 <= mediap <= 40:
            print (("{:.2f}").format(mediap))
            print ("Reprovado")

        elif 40 <= mediap <= 70:
            print (("{:.2f}").format(mediap))
            print("Final")

elif tipo == ("h"):
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    if 1 <= nota1 <=100 and 1 <= nota2 <=100 and 1 <= nota3 <=100:
        mediah = 3/(1/nota1+1/nota2+1/nota3)
        if 70 <= mediah <= 100:
            print(("{:.2f}").format(mediah))
            print ("Aprovado")

        elif 0 <= mediah <= 40:
            print (("{:.2f}").format(mediah))
            print ("Reprovado")

        elif 40 <= mediah <= 70:
            print (("{:.2f}").format(mediah))
            print("Final")

else:
    print("Escolha um tipo de media valida.")