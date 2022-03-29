from posixpath import abspath
from time import sleep
from os import system, path
from platform import system as so
import pygame
import yaml



musicas_disponiveis = {
    '1':'BatmanTheme.mp3' ,
    '2':'DUSK_TILL_DAWN.mp3',
    '3':'Gladiator_Im_Maximus_Decimus_Denirius.MP3' ,
    '4':'Guns_N_Roses_Patience.mp3',
    '5':'LUCKHAOS_Faccao_Trava_Zap.mp3',
    '6':'LUCKHAOS_TORTURA_PENIANA.mp3',
    '7':'LUCKHAOS_Uniao_Flasco.mp3',
    '8':'Tokyo_Drift.mp3',
    '9':'UDR_666_Orgia_de_Traveco.mp3',
    '10':'WB_Bora.mp3'
}


# CLEAR
def clear():
    if so() == 'Linux':
        system('clear')

    if so() == 'Windows':   
        system('cls')


def player_sistema():
    print(yaml.dump(musicas_disponiveis, sort_keys=False, default_flow_style=False))
    print('DIGITE A OPÇÃO DESEJADA')
    musica = input('-> ')

    absolutepath = path.abspath(__file__)

    pygame.init()
    pygame.mixer.init()
    #Adicionar o caminho completo do sistema ate a pasta music

    if so() == 'Linux':
        #pygame.mixer.music.load(f'/home/andrefernandes/andrefernandes/pythonzin/pythonfiles/calculadora/music/{musicas_disponiveis[musica]}')
        pygame.mixer.music.load(f'{absolutepath}'.replace('/calculadora.py', '')+f'/music/{musicas_disponiveis[musica]}')
        pygame.mixer.music.play()
        pygame.event.wait()

    elif so() == 'Windows':

        pygame.mixer.music.load(f'{absolutepath}'.replace('\calculadora.py', '')+f'\music\{musicas_disponiveis[musica]}')
        pygame.mixer.music.play()
        pygame.event.wait()

# IMPORTA O PLAYER ONLINE
def player_online():
    import playeronline


# PLAYER DE MÚSICA
def music_player():
    # PERGUNTA SE QUER MÚSICA
    print('O senhor gostaria de ouvir uma música? S/N')
    print('-' * 50)
    p2 = input('-> ').upper()
    # ERRO
    if p2 not in ['SIM', 'NÃO', 'NAO', 'S', 'N']:
        print('\n   ERRO\n', 'TENTE NOVAMENTE')

    # RESPOSTA NÃO
    elif p2 in ['N', 'NAO', 'NÃO']:
        clear()
        print('Ok mestre, gostaria de sair? S/N')
        print('-' * 50)
        s = input('-> ').upper()

        # ERRO
        if s not in ['S', 'N']:
            print('ERRO\n', 'TENTE NOVAMENTE')

        # RESPOSTA SIM
        if s == 'S':
            print('Adeus, Mestre\n', '   SAINDO')
            sleep(2)
            return

        # RESPOSTA NÃO lucius fox
        if s == 'N':
            print('OK')
            clear()
            music_player()

    # RESPOSTA SIM
    elif p2 in ['1', 'S', 'SIM']:
        print('Pois não, Senhor.')
        sleep(1)
        clear()
        print('O senhor gostaria de ouvir músicas online, ou do sistema?')
        resposta = str(input('-> ')).upper()
        #FAZ ABRIR PLAYER ONLINE
        if resposta == 'ONLINE':
            clear()
            player_online()
            
        #FAZ ABRIR PLAYER DO SISTEMA
        if resposta == 'SISTEMA':
            clear()
            player_sistema()
            

# MENU
def menu():
    clear()
    print('Bem vindo, Mestre')

    # PERGUNTA COMO FOI O DIA
    print('Como foi o seu dia?')
    p1 = input('-> ').upper()

    # RESPOSTA POSITIVA
    if p1 in ['BOM', 'LEGAL', 'PRODUTIVO', 'EMPOLGANTE', 'EMOCIONANTE', 'IRADO', 'QUENTE', 'CRUEL', 'PIKA', 'INCRÍVEL',
              'NICE', 'MASSA', 'MUITO MASSA', 'EXCELENTE']:
        clear()
        print('Que bom, Patrão André!\n')

        # PLAYER DE MUSICA
        music_player()

    # RESPOSTA NEGATIVA
    if p1 in ['RUIM', 'UMA MERDA', 'BOSTA', 'HORRÍVEL', 'CHATO', 'MONÓTONO', 'MONOTONO', 'PODRE', 'TEDIOSO', 'UM TÉDIO',
              'UM TEDIO', 'CHATO PKRL', 'DEPLORÁVEL', 'MUITO RUIM', 'CU', 'UM CU']:
        clear()
        print('Uma pena, Senhor.')
        sleep(1.8)

        print('Senhor, acho que tenho uma solução:')
        music_player()


while True:
    clear()
    x = input('''Selecione a opção:
[ 1 ]Soma
[ 2 ]Subtração
[ 3 ]Multiplicação
[ 4 ]Divisão
[ 5 ]Potência
[ 6 ]Raiz
-> ''').upper()

    if x not in ['1', '2', '3', '4', '5', '6', '7', '8', 'LUCIUS FOX', 'SAIR', 'EXIT', 'CAPE THE CAT', 'QUIT']:
        print('ERRO\n   TENTE NOVAMENTE')
        input()

    #SOMA    
    if x == '1':
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('\nSegundo número: '))
        print(f'\n{n1} + {n2} = \033[31m{n1+n2:.3}\033[m')
        input()

    #SUBTRAÇÃO
    elif x == '2':
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('\nSegundo número: '))
        print(f'\n{n1} - {n2} = \033[31m{n1-n2:.3}\033[m')
        input()

    #MULTIPLICAÇÃO
    elif x == '3': 
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('\nSegundo número: '))
        print(f'\n{n1} x {n2} = \033[31m{n1*n2:.3}\033[m')
        input()

    #DIVISÃO
    elif x == '4':
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('\nSegundo número: '))
        print(f'\n{n1} / {n2} = \033[31m{n1/n2:.3}\033[m')
        input()

    #POTÊNCIA
    elif x == '5':
        n1 = float(input('\nBase: '))
        n2 = float(input('\nExpoente: '))
        print(f'\n{n1}^{n2} = \033[31m{n1**n2:.3}\033[m')    
        input()

    #RAÍZ
    elif x == '6':
        n1 = float(input('\nRadicando: '))
        n2 = float(input('\nÍndice: '))
        print(f'\n√{n1} = \033[31m{n1 ** (1/n2):.3}\033[m')
        input()

    elif x == 'LUCIUS FOX':
        menu()

    if x in ['SAIR', 'EXIT', '8', 'QUIT', 'CAPE THE CAT']:
        print('Adeus!')
        sleep(0.3)
        exit()
    
