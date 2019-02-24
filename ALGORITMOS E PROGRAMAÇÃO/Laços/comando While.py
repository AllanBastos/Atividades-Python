receber_nota = input("rebeber nota? (s) ou (n)")
soma_notas = 0

notas = int(input("Insira sua nota:"))

quantidade_notas = 0

while receber_nota == ("s"):

    soma_notas += notas
    receber_nota = input("rebeber nota? (s) ou (n)")
    notas = int(input("Insira sua nota:"))

    quantidade_notas +=1

media = soma_notas / quantidade_notas
print("Sua media é ", media)