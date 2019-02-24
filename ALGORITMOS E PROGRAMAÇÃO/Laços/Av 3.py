idade = int(input())
sexo = (input())
peso = float (input())
anoPD = int(input())
quant_D_Ano = int(input())
ultimaD = int(input())
APTIDAO = " "
if 16 <= idade <= 69:
    if peso > 50.0:
        if sexo == "m" and quant_D_Ano <= 4 and ultimaD <= 7:
            APTIDAO = "Pode ser doador"
        elif sexo == "f" and quant_D_Ano <= 3 and ultimaD <= 6:
            APTIDAO = 'Pode ser doadora'
        else:
            APTIDAO = "Nao pode doar sangue"

else:
    APTIDAO = "Nao pode doar sangue"

print(APTIDAO)