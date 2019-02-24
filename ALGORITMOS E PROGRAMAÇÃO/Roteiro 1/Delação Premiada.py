crimeDelator = str(input())

if crimeDelator == "roubo" or crimeDelator == "tráfico" or crimeDelator == "homicídio":

        if (crimeDelator == "roubo") or (crimeDelator == "tráfico"):

            valorX9 = int(input())

            crimeDelatado = input()


        elif (crimeDelator == "homicídio"):

            crimeDelatado = input()

        if (crimeDelatado !=  'roubo' and crimeDelatado != "homicídio" and crimeDelatado != "tráfico"):

            print("Crime inválido.")

        else:



            if (crimeDelatado == "roubo") or (crimeDelatado == "tráfico"):

                ValorDelatado = int(input())



            if (crimeDelator == "roubo" or crimeDelator == "tráfico") and (crimeDelatado == "homicídio"):
                print("Delação concedida.")

            elif ((crimeDelator == "roubo" and (((crimeDelatado == "roubo") )))):
                    f = valorX9*5
                    if  (ValorDelatado > f):
                        print("Delação concedida.")
                    else:
                        print("Delação rejeitada.")


            elif (crimeDelator == "roubo")  and (crimeDelatado == "tráfico" ):
                    g = valorX9*3
                    if ValorDelatado > g:
                        print("Delação concedida.")
                    else:
                        print("Delação rejeitada.")

            elif ((crimeDelator == "tráfico")  and ((crimeDelatado == "tráfico") and (ValorDelatado > valorX9*5))):
                print("Delação concedida.")

            elif (crimeDelator == "homicídio")  and (crimeDelatado == "homicídio" ):
                print("Delação concedida.")
            else:
                print("Delação rejeitada.")


else:
    print("Crime inválido.")