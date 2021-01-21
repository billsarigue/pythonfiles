from os import system
from platform import system as so

def clear():
    if so() == 'Linux':
        system('clear')

    elif so() == 'Windows':
        system('cls')


def main_loop():
    print('Qual o seu nome?')
    nome = str(input('-> ')).upper()

    if nome == 'PEDRO':
        print('Que nome gay!')
        input()
    elif nome == 'LUCIUS FOX':
        menu()
    else:
        print('Que nome legal!')
        input()
    return


def menu():
    print('Olá, Mestre!')
    input()



while True:
    clear()
    main_loop()
    
