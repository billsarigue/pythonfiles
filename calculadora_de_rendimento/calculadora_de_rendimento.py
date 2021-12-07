from deps import *


clear()



while True:

    abertura()		
    print('[1] JUROS COMPOSTOS \n' + '[2] JUROS SIMPLES\n' + '[3] SAIR')

    pergunta = str(input('\n-> ')).lower()

    if pergunta not in ['1','2','3','sair','exit']:

        print('ERRO, TENTE NOVAMENTE')
        input()
        clear()

    elif pergunta == '1':

        clear()
        juros_compostos()

    elif pergunta == '2':
        clear()
        juros_simples()

    elif pergunta in ['3','sair','exit']:

        clear()
        print('ADEUS!')
        break

#clear()
