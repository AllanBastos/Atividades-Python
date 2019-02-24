dia = str(input())
preço = float(input())
opçao = str(input())
produto = input()

if dia == "seg"  and opçao == "ouro":
    s = preço / 2
    print ("O preco do produto", produto , "no dia seg eh ", s)


elif dia == "ter"  and opçao == "ouro":
    s = preço / 2
    print ("O preco do produto", produto , "no dia ter eh ", "{:.2f}" .format(s))

elif dia == "qua"  and opçao == "ouro":
    s = preço / 2
    print ("O preco do produto", produto , "no dia qua eh ","{:.2f}" .format(s))

elif dia == "qui" and 10 <= preço <= 100:
    s2 = preço/3
    print ("O preco do produto", produto , "no dia qui eh ", "{:.2f}" .format(s2) )

elif dia == "sex" and 10 <= preço <= 100:
    s2 = preço/3
    print ("O preco do produto", produto , "no dia sex eh ", "{:.2f}" .format(s2) )

elif dia == "sab" and opçao == "prata":
    s3 = preço*3
    print ("O preco do produto", produto , "no dia sex eh ", "{:.2f}" .format(s3) )

else:
    s4 = preço*2
    print("O preco do produto", produto , "no dia", dia,"eh", "{:.2f}" .format(s4))

