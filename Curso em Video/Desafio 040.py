n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2)/2
print('Quem tirou {:.1f} e {:.1f} tem a media {:.1f}'.format(n1, n2, media))
if media < 5:
    print('\033[31mO aluno esta REPROVADO\033[m')
elif 5 <= media < 7:
    print('\033[33mO aluno esta de RECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[32mO aluno esta APROVADO\033[m')

