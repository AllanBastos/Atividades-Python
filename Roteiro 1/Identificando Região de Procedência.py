codigo = int(input())
if codigo == 1:
    print("Nordeste")
elif codigo == 2:
    print("Norte")
elif codigo == 3 or codigo == 4:
    print("Centro-Oeste")
elif  5 <= codigo <= 9 :
    print("Sul")
elif 10 <= codigo <= 15 :
    print("Sudeste")
else:
    print("Regiao nao encontrada")