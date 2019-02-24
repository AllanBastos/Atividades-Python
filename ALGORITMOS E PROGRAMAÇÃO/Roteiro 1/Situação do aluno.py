nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

media = (nota1+nota2+nota3)/3

if 70<= media <= 100:
    print(("A media do aluno foi"), ("{:.2f}").format(media), ("e ele foi APROVADO"))

elif 0<= media <= 40:
    print(("A media do aluno foi"), ("{:.2f}").format(media), ("e ele foi REPROVADO"))

elif 40<= media <= 70:
    print(("A media do aluno foi"), ("{:.2f}").format(media), ("e ele foi FINAL"))

else:
    print("Media invalida")
