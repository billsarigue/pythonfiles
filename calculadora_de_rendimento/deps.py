from os import system
from platform import system as so
from art import *


cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m'}


def clear():
    if so() == 'Linux':
        system('clear')

    if so() == 'Windows':
        system('cls')


def abertura():
    print('-'*33)
    tprint('CALCULADORA DE',font="small")
    tprint('RENDIMENTO',font="small")


def main():
    valor_inicial = float(input('INVESTIMENTO INICIAL: '))
    taxa_ao_mes = float(input('TAXA AO MÊS: '))
    taxa_ao_mes = taxa_ao_mes / 100
    tempo_em_mes = int(input('TEMPO EM MESES: '))
    valor_final = valor_inicial * (1+taxa_ao_mes)**tempo_em_mes
    lucro = valor_final - valor_inicial
    print()
    print('_'*35)
    print(f'\nVALOR FINAL: {cores["ciano"]}R${valor_final:.2f}{cores["limpa"]}')
    print(f'LUCRO: {cores["verde"]}R${lucro:.2f}{cores["limpa"]}')
    print('_'*35)
    print()
    input()