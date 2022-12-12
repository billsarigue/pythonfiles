import pyttsx3
from os import system
from platform import system as so


def clear():
    if so == 'Linux':
        system('clear')

    if so == 'Windows':
        system('cls')

clear()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', 'brazil')

engine.setProperty('rate', 150)

print('OLÁ! DIGITE AQUI O QUE VOCÊ QUER QUE EU DIGA!')

while True:
    clear()
    frase = str(input('\n-> '))
    
    if frase == 'exit':
        engine.say('Adeus!')
        engine.runAndWait()
        exit()
    
    else:
        engine.say(frase)


    engine.runAndWait()
    
