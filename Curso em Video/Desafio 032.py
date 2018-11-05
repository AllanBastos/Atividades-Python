def bi6(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return 'é'
    else:
        return 'NÃO é'
from datetime import date

ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year

print('O ano {} {} BISSEXTO'.format(ano, bi6(ano)))
