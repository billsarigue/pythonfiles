import math
from os import system
from platform import system as so


def clear():
    if so() == 'Linux':
        system('clear')

    if so() == 'Windows':
        system('cls')


cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m'}
clear()


def menu():
    print('''________________________________________________________________
    [V] Velocidade média 
    
    [S] Deslocamento
    
    [T] Variação de tempo
    
    [A] Aceleração
    
    [F] Força
    
    [C] Energia cinética 
    
    [G] Energia potencial gravitacional
    
    [P] Potência
    
    [D] Dilatação linear
    
    [TR] Trabalho
    
    [SF] Função horária (final) 
    
    [SO] Função horária (inicial) 
    
    [CO] Lei dos cossenos
    
    [TC] Conversão Farenheit -> Celcius
    
    [TF] Conversão Celcius -> Farenheit
    
    [VC] Conversão celsius - fahrenheit - celsius (variação)
    ________________________________________________________________
    ''')
    print(f'[{cores["amarelo"]}+{cores["limpa"]}] Para sair digite {cores["ciano"]}[0]\n')


fim = 0
while fim != 1:
    print(f'{cores["azul"]}Bem vindo à calculadora de fisíca!{cores["limpa"]}\n')
    menu()
    print(f'{cores["vermelho"]}IMPORTANTE! USE MEDIDAS DO SI!')

    formula = str(input(f'\n{cores["azul"]}Qual fórmula você quer calcular?{cores["limpa"]} -> ')).strip().upper()[0:2]
    clear()
    while formula not in 'S''T''A''F''C''G''TR''P''SF''SO''CO''TC''TF''VC''VF''D':
        menu()
        print(f'{cores["vermelho"]}IMPORTANTE! USE MEDIDAS DO SI!')
        formula = str(input(f'\n{cores["azul"]}Qual fórmula você quer calcular?{cores["limpa"]} ')).strip().upper()[0:2]
    if formula in 'V':
        x = 'q'
        s = float(input('Qual o deslocamento do corpo? '))
        t = float(input('\nQual o tempo percorrido pelo corpo? '))
        v = s / t
        print(f'\nA velocidade média do corpo foi de {v:.2f} metros por segundo.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/n]')).strip().upper()
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'T':
        x = 'q'
        v = float(input('Qual a velocidade média do corpo? '))
        s = float(input('\nQual o deslocamento do corpo? '))
        t = s / v
        print(f'\nO tempo percorrido foi de {t:.2f} segundos.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'S':
        x = 'q'
        v = float(input('Qual a velocidade média do corpo? '))
        t = float(input('\nQual o tempo percorrido pelo corpo? '))
        s = v * t
        print(f'\nO deslocamento percorrido foi de {s:.2f} metros.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'A':
        x = 'q'
        v = float(input('Qual a velocidade média do corpo? '))
        t = float(input('\nQual o tempo percorrido pelo corpo? '))
        a = v / t
        print(f'\nA aceleração média do corpo foi de {a:.2f} metros por segundo ao quadrado.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'F':
        x = 'q'
        m = float(input('Qual a massa do corpo? '))
        a = float(input('\nQual a aceleração média do corpo? '))
        f = m * a
        print(f'\nA força aplicada no corpo é de {f:.2f} newtons.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'C':
        x = 'q'
        m = float(input('Qual a massa do corpo? '))
        v = float(input('\nQual a velocidade média do corpo? '))
        ec = (m * math.pow(v, 2)) / 2
        print(f'\nA energia cinética do corpo é de {ec:.2f} joules.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'G':
        x = 'q'
        m = float(input('Qual a massa do corpo? '))
        g = float(input('\nQual a aceleração gravitacional sofrida pelo corpo? '))
        h = float(input('\nQual a altura do corpo em relação ao solo? '))
        epg = m * g * h
        print(f'\nA energia potencial do corpo foi de {epg:.2f} Joules.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'TR':
        x = 'q'
        f = float(input('Qual a força resultante do corpo? '))
        d = float(input('\nQual o deslocamento do corpo? '))
        cos = int(input('\nQual o ângulo do corpo em relação ao solo?'))
        t = f * d * math.cos(math.radians(cos))
        print(f'\nO trabalho do corpo é de {t:.2f} joules.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'P':
        x = 'q'
        tr = float(input('Qual o trabalho do corpo? '))
        te = float(input('\nQual o tempo percorrido? '))
        p = tr / te
        print(f'\nA potência do corpo é de {p:.2f} watts.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'SF':
        x = 'q'
        o = float(input('Qual a distância inicial do corpo? '))
        v = float(input('\nQual a velocidade do corpo? '))
        t = float(input('\nQual o tempo percorrido? '))
        s = o + v * t
        print(f'\nA distância final do corpo é de {s:.2f} metros.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'SO':
        x = 'q'
        s = float(input('Qual a distância final do corpo? '))
        v = float(input('\nQual a velocidade média do corpo? '))
        t = float(input('\nQual o tempo percorrido? '))
        o = v * t - s
        print(f'\nA distância inicial do corpo é de {o:.2f} metros.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'CO':
        x = 'q'
        a = float(input('Qual a medida do primeiro vetor? '))
        b = float(input('\nQual a medida do segundo vetor? '))
        c = int(input('\nQual o ângulo entre os lados?'))
        d = math.sqrt(pow(a, 2) + pow(b, 2) + 2 * a * b * math.cos(math.radians(c)))
        print(f'\nO vetor resultante vale {d:.2f}.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'TF':
        x = 'q'
        c = float(input('Qual a temperatura em celsius? '))
        f = (9*c+160)/5
        print(f'\nA temperatura em fahrenheit é de {f:.2f} °F.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'TC':
        x = 'q'
        f = float(input('Qual a temperatura em fahrenheit? '))
        c = 5*(f-32)/9
        print(f'\nA temperatura em celsius é de {c:.2f} °C.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'VC':
        x = 'q'
        f = float(input('Qual a variação em fahrenheit? '))
        c = (f / 9) * 5
        print(f'\nA variação em celsius é de {c} °C.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'VF':
        x = 'q'
        c = float(input('Qual a variação em celsius? '))
        f = (c / 5) * 9
        print(f'\nA variação em fahrenheit é de {c} °F.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
    elif formula in 'D':
        x = 'q'
        o = float(input('Qual o comprimento inicial do corpo? '))
        a = float(input('\nQual a constante de temperatura do corpo? '))
        t = float(input('\nQual a variação de temperatura do corpo? '))
        c = o * a * t
        print(f'\nA variação do comprimento do corpo foi de {c} metros.')
        while x not in 'SN':
            x = str(input('\nDeseja continuar? [S/N]')).strip().upper()[0]
            if x in 'S':
                print('\nVamos lá!')
            else:
                print('\nObrigado e volte sempre!')
                fim = 1
print(f'\n{cores["ciano"]}Obrigado por usar a calculadora!')
