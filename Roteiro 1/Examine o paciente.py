temperatura = float(input())
SN = str(input())

if temperatura >= 37 and SN == "S":
    print("Exames Especiais")

elif temperatura >= 37 and SN == "N":
    print("Exames Basicos")

elif temperatura < 37 and   SN == "N":
    print("Liberado")

elif temperatura < 37  and  SN == "S":
    print("Exames Basicos")

else:
    print("Erro")