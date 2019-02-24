import datetime



ano_nacimento = int(input('Qual seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = (ano_atual - ano_nacimento)
tempo = (ano_atual - ano_nacimento) - 18
while True:
    sexo = input('Qual é o seu sexo ?\n[ M ] para Masculino\n[ F ] para Feminino\n').upper()


    if sexo not in ('F, M'):
        print('Opção invalida tente novamente!')
    else:
        if sexo == 'M':
            print('Quem nasceu em {} tem {} em {}'.format(ano_nacimento, idade, ano_atual))
            if ano_nacimento > ano_atual:
                print('\033[31;1mInsira um ano valido e tente novamente\033[m')

            elif (ano_atual - ano_nacimento) < 18:
                print('\033[1;36mAinda falta {} ano(s) para você poder se alisata.\033[m'.format(tempo*(-1)))
                print('Seu alistamento será em {}'.format(ano_atual + (tempo*(-1))))
            elif (ano_atual - ano_nacimento) == 18:
                print('\033[1;33mEsta na hora de você se alistar!\033[m')

            else:
                print('\033[1;31mJá se passou {} ano(s) de você ter que se alistar, procure uma'
                        ' junta militar mais perto de sua casa e se aliste.\033[m'.format(tempo))
                print('Seu alistamento foi em {}'.format(ano_atual-(tempo)))
        elif sexo == 'F':
            print('Lembre-se Mulher não é obrigatório o alistamento!')
            continuar = input('Mesmo assim você deseja continuar? S/N' ).upper()

            if continuar == 'S':
                print('Quem nasceu em {} tem {} em {}'.format(ano_nacimento, idade, ano_atual))
                if ano_nacimento > ano_atual:
                    print('\033[31;1mInsira um ano valido e tente novamente\033[m')

                elif (ano_atual - ano_nacimento) < 18:
                    print('\033[1;36mAinda falta {} ano(s) para você poder se alisata.\033[m'.format(tempo * (-1)))
                    print('Seu alistamento será em {}'.format(ano_atual + (tempo * (-1))))
                elif (ano_atual - ano_nacimento) == 18:
                    print('\033[1;33mEsta na hora de você se alistar!\033[m')

                else:
                    print('\033[1;31mJá se passou {} ano(s) de você ter que se alistar, procure uma'
                          ' junta militar mais perto de sua casa e se aliste.\033[m'.format(tempo))
                    print('Seu alistamento foi em {}'.format(ano_atual - (tempo)))
            else:
                print('Ok então, tenha um bom dia!')
        break
