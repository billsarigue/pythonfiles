from os import system
from platform import system as so
from pyfiglet import Figlet
from math import sqrt

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

    render('BHASKARA')

    a = float(input('''\nQual o A da equação?

    }> '''))

    b = float(input('''\nQual o B da equação?

    }> '''))

    c = float(input('''\nQual o C da equação?

    }> '''))

    delta = b**2 -4*a*c
    rdelta = sqrt(delta)

    x1 = (-b + rdelta) / (2 * a)
    x2 = (-b - rdelta) / (2 * a)

    print('\n\n\nX = -b +-√b²-4ac')
    print('    ------------')
    print('         2a')


    print('\n\n-------------')
    print('\033[31m', f'Delta = {delta}', '\033[0;0m')
    print('\033[31m', f'√Delta = {rdelta}', '\033[0;0m')
    print('-------------')

    input()


    print('\033[32m', f'''

        RAÍZES:
 _____________________

  X' = {x1}

  X" = {x2}               
 _____________________
    ''','\033[0;0m' )
    
    input()

