from time import sleep
from os import system
from platform import system as so



#CLEAR
def clear():

	if so() == 'Linux':
		system('clear')

	if so() == 'Windows':
		system('cls')


#IMPORTA O PLAYER ONLINE
def player_online():
	import playeronline


#PLAYER DE MÚSICA
def music_player():

	#PERGUNTA SE QUER MÚSICA
	print('O senhor gostaria de ouvir uma música? S/N')
	print('-'*50)
	p2 = input('-> ').upper()
	#ERRO
	if p2 not in ['SIM', 'NÃO', 'NAO', 'S', 'N']:
		print('\n   ERRO\n', 'TENTE NOVAMENTE')

	#RESPOSTA NÃO
	if p2 in ['N', 'NAO', 'NÃO']:
		clear()
		print('Ok mestre, gostaria de sair? S/N')
		print('-'*50)
		s = input('-> ').upper()

		#ERRO
		if s not in ['S', 'N']:
			print('ERRO\n', 'TENTE NOVAMENTE')
		
		#RESPOSTA SIM
		if s == 'S':
			print('Adeus, Mestre\n', '   SAINDO')
			sleep(2)
			return

		#RESPOSTA NÃO
		if s == 'N':
			print('OK')
			clear()
			music_player()
	
	#RESPOSTA SIM	
	if p2 in ['1', 'S', 'SIM']:
		print('Pois não, Senhor.')
		sleep(1)
		clear()
		print('O senhor gostaria de ouvir músicas online, ou do sistema?')
		resposta = str(input('-> ')).upper()
		if resposta == 'ONLINE':
			clear()
			player_online()



#MENU
def menu():
	clear()
	print('Bem vindo, Mestre')

	#PERGUNTA COMO FOI O DIA
	print('Como foi o seu dia?')
	p1 = input('-> ').upper()

	#RESPOSTA POSITIVA
	if p1 in ['BOM', 'LEGAL', 'PRODUTIVO', 'EMPOLGANTE', 'EMOCIONANTE', 'IRADO', 'QUENTE', 'CRUEL', 'PIKA', 'INCRÍVEL', 'NICE','MASSA','MUITO MASSA' ]:
		clear()
		print('Que bom, Patrão André!\n')

		#PLAYER DE MUSICA
		music_player()

	#RESPOSTA NEGATIVA
	if p1 in ['RUIM','UMA MERDA','BOSTA','HORRÍVEL','CHATO','MONÓTONO','MONOTONO','PODRE','TEDIOSO','UM TÉDIO','UM TEDIO','CHATO PKRL','DEPLORÁVEL','MUITO RUIM','CU','UM CU']:
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

	if x not in ['1', '2', 'LUCIUS FOX','SAIR','EXIT','CAPE THE CAT']:
		print('ERRO\n   TENTE NOVAMENTE')
		input()
	if x == '1':
		n1 = float(input('Primeiro número: '))
		n2 = float(input('Segundo número: '))
		print('A soma de {} com {} é \033[31m{}\033[m'.format(n1, n2, n1+n2))
		input()

	if x == '2':
		n1 = float(input('Primeiro número: '))
		n2 = float(input('Segundo número: '))
		print('A subtração de {} de {} é \033[31m{}\033[m'.format(n2, n1,n1-n2)) 
		input()
	if x == 'LUCIUS FOX':
		menu()

	if x in ['SAIR','EXIT','CAPE THE CAT']:
		print('Adeus!')
		sleep(0.7)
		exit()
		
		
		