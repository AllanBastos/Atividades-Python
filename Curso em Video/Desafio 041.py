import datetime
nascimento = int(input('Em qual ano você nasceu ? '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
cat = ''
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JÚNIOR'
elif idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'

print('O atleta tem {} anos.\nClassificação: {}'.format(idade, cat))