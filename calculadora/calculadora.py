from time import sleep
from os import system
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

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(f'music\{musicas_disponiveis[musica]}')
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

        # RESPOSTA NÃO
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
              'NICE', 'MASSA', 'MUITO MASSA']:
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
    x = input('''Selecione  opção:
[ 1 ]Soma
[ 2 ]Subtração
-> ''').upper()

    if x not in ['1', '2', 'LUCIUS FOX', 'SAIR', 'EXIT', 'CAPE THE CAT']:
        print('ERRO\n   TENTE NOVAMENTE')
        input()
    if x == '1':
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        print('A soma de {} com {} é \033[31m{}\033[m'.format(n1, n2, n1 + n2))
        input()

    if x == '2':
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        print('A subtração de {} de {} é \033[31m{}\033[m'.format(n2, n1, n1 - n2))
        input()
    if x == 'LUCIUS FOX':
        menu()

    if x in ['SAIR', 'EXIT', 'CAPE THE CAT']:
        print('Adeus!')
        sleep(0.3)
        exit()


