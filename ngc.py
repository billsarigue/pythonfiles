import pyttsx3
from os import system


def clear():
    system('clear')

clear()

engine = pyttsx3.init()

engine.setProperty('voice', 'brazil')

engine.setProperty('rate', 150)

print('OLÁ! DIGITE AQUI O QUE VOCÊ QUER QUE EU DIGA!')


engine.say('OLÁ! DIGITE AQUI O QUE VOCÊ QUER QUE EU DIGA!')

engine.runAndWait()

while True:
    clear()
    print('OLÁ! DIGITE AQUI O QUE VOCÊ QUER QUE EU DIGA!')
    frase = str(input('\n-> '))
    engine.say(frase)












    engine.runAndWait()