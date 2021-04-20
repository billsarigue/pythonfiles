from deps import *


clear()

abertura()

while True:

    print('[1] JUROS COMPOSTOS \n' + '[2] JUROS SIMPLES\n' + '[3] SAIR')

    pergunta = str(input('\n-> ')).lower()

    if pergunta not in ['1','2','3','sair']:

        print('ERRO, TENTE NOVAMENTE')

    elif pergunta == '1':

        clear()
        juros_compostos()

    elif pergunta == '2':
        clear()
        juros_simples()

    elif pergunta == '3':

        clear()
        print('ADEUS!')
        break

#clear()