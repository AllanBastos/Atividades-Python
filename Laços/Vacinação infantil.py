ano = int(input())
inter= int(input())
cont = ano
for n in range(3):
    ano += inter
    cont += inter
    print(cont,end=" ")