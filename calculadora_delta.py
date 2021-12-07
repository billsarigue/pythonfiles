from os import system
from platform import system as so
from pyfiglet import Figlet

def clear():
    if so() == 'Linux':
        system('clear')

    if so() == 'Windows':
        system('cls')


def render(text):
    f = Figlet()
    print(f.renderText(text))


while True:
    clear()

    render('DELTA')


    a = float(input('Digite o [A] da equação: '))
    b = float(input('Digite o [B] da equação: '))
    c = float(input('Digite o [C] da equação: '))

    delta = b**2 - 4*a *c

    print('_'*20)
    print()
    print('\033[32m' , delta , '\033[0;0m')
    print('_'*20)
    input()