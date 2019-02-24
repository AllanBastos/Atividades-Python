letra = str(input())

igual1 =  len(letra)

if igual1 != 1:

    print("1 caractere, por favor!")
elif letra == "a" or letra == "A" or letra =="e" or letra =="E" or letra =="i" or letra =="I" or letra =="o" or letra =="O" or letra =="u" or letra == "U":
    print("Eh vogal")

else:
 print("Nao eh vogal")
