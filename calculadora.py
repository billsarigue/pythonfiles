from time import sleep

#PLAYER DE MÚSICA
def music_player():
	#PERGUNTA SE QUER MÚSICA
	p2 = input('''O senhor gostaria de ouvir uma música?
[0] Não
[1] Sim
''').upper()
	#ERRO
	if p2 not in ['0', '1', 'SIM', 'NÃO', 'NAO', 'S', 'N']:
		print('ERRO\n', '   TENTE NOVAMENTE')

	#RESPOSTA NÃO
	if p2 in ['0', 'N', 'NAO', 'NÃO']:
		s = input('Ok mestre, gostaria de sair? S/N').upper()

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
			input()
	
	#RESPOSTA SIM	
	if p2 in ['1', 'S', 'SIM']:
		print('Pois não, Senhor.')
		sleep(1.5)
		print('''O senhor gostaria de ouvir músicas online, ou do sistema?'''

#MENU
def menu():
	print('Bem vindo, Mestre')

	#PERGUNTA COMO FOI O DIA
	p1 = input('Como foi o seu dia?').upper()

		#RESPOSTA POSITIVA
	if p1 in ['BOM', 'LEGAL', 'PRODUTIVO', 'EMPOLGANTE', 'EMOCIONANTE', 'IRADO', 'QUENTE', 'CRUEL', 'PIKA', 'INCRÍVEL', 'NICE' ]:
	        print('Que bom, Patrão André!\n')

		#PERGUNTA SE QUER MÚSICA
		print('Gostaria de ouvir uma música?')
		per = str(input('-> '))
	

		print('-'*40)
		m = input('-> ').upper()
		
		#ERRO
		if m not in ['0', '1', 'ONLINE', 'SISTEMA']:
			print('ERRO\n', '   TENTE NOVAMENTE')

		#ONLINE
		print('Certamente, Senhor')
		sleep(1.5)
		musica = input('DIGITE AQUI O NOME DA SUA MÚSICA:')
			








while True:
	x = input('''Selecione  opção:
[ 1 ]Soma
[ 2 ]Subtração
-> ''').upper()

	if x not in ['1', '2', 'LUCIUS FOX']:
		print('ERRO\n   TENTE NOVAMENTE')
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
		
		
		