import sqlite3
from time import sleep
from pyfiglet import Figlet
from random import choice


def render(text):
    f = Figlet()
    print(f.renderText(text))

adeus = ['ADIÓS', 'GOODBYE', 'AU REVOIR', 'ARRIVEDERCI', 'AUF WIEDERSEHEN', 'ADEUS', 'DAAG', 'αντίο'.upper() , 'VALE', 'Nakemiin'.upper(), 'adjo'.upper(), 'FARVEL', 'Do svidaniya'.upper(), 'Do widzenia'.upper() ]
wallpapers = ['-SECUROSERV-', '*SECUROSERV*', '¬SECUROSERV¬', '-S3CUR0S3RV-', '*SECUROSERV*', '¬S3CUR0S3RV¬']
lista = ['220304', 'lucius fox']
lista = True
Senha_mestra = input('Digite sua senha mestra: ')
if (Senha_mestra != '220304') and (Senha_mestra != 'lucius fox'):
    print('''         ERRO
    SENHA INVÁLIDA    
    ''')
    sleep(1.5)
    print('       Saindo...')
    sleep(1.5)
    exit()

if (Senha_mestra == '220304') or (Senha_mestra == 'lucius fox'):
    c = sqlite3.connect('passwords.db')

    cursor = c.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        service TEXT NOT NULL,    
        username TEXT N0T NULL,
        password TEXT NOT NULL
    );
    ''')


    def nova_senha(service, username, password):
        cursor.execute(f'''
            INSERT INTO users (service, username, password)
            VALUES ('{service}', '{username}', '{password}')
        ''')
        c.commit()


    def mostrar_serviço():
        cursor.execute(f'''
            SELECT service FROM users;
        ''')
        for service in cursor.fetchall():
            print(service)


    def obter_senha(service):
        cursor.execute(f'''
            SELECT username, password FROM users
            WHERE service = '{service}'
        ''')
        if cursor.rowcount == 0:
            print('Serviço não cadastrado (use [2] para listar os serviços).')
        else:
            for user in cursor.fetchall():
                print(user)


    def menu():
        print('-' * 30)
        print(('-' * 13) + 'MENU' + ('-' * 13))
        print(' [1] Inserir nova senha')
        print(' [2] Listar dados salvos')
        print(' [3] Recuperar senha')
        print(' [4] Sair')
        print('-' * 30)


    def menu_admin():
        print('-' * 30)
        print(('-' * 13) + 'MENU' + ('-' * 13))
        print(' [1] Inserir nova senha')
        print(' [2] Listar dados salvos')
        print(' [3] Recuperar senha')
        print(' [4] Sair')
        print(' [root] Admin')
        print('-' * 30)


    while True:
        while Senha_mestra == 'lucius fox':
            render('fsociety')
            menu_admin()
            op = input('-> ')
            if op not in ['1', '2', '3', '4', 'root']:
                print('OPÇÃO INVÁLIDA!')
                print('Tente novamente')
                sleep(1.5)
                continue
            if op == '1':
                print('-' * 20, '\n')
                service = input('Qual o nome do serviço? -> ')
                username = input('Qual o nome de usuário? -> ')
                password = input('Qual a sua senha? -> ')
                nova_senha(service, username, password)
                print('-' * 20, '\n')
                input('PRESSIONE ENTER PARA CONTINUAR')

            if op == '2':
                print('-' * 20, '\n')
                mostrar_serviço()
                print('-' * 20, '\n')
                input('PRESSIONE ENTER PARA CONTINUAR')

            if op == '3':
                print('-' * 20, '\n')
                mostrar_serviço()
                service = input('De qual serviço você gostaria de recuperar a senha? -> ')
                obter_senha(service)
                print('-' * 20, '\n')
                input('PRESSIONE ENTER PARA CONTINUAR')

            if op == '4':
                render(choice(adeus))
                print('-' * 20)
                print('OBRIGADO POR USAR ESTE SERVIÇO!')
                print(('   Created by: André Fernandes'))
                print('-' * 20)
                input('PRESSIONE ENTER PARA CONTINUAR')
                break
            if op == 'root':
                print('BEM, VINDO MESTRE')
                import veia
                input('PRESSIONE ENTER PARA CONTINUAR')

        render(choice(wallpapers))
        print(' By: André Fernandes')
        menu()
        op = (input('-> '))
        if op not in ['1', '2', '3', '4']:
            print('OPÇÃO INVÁLIDA!')
            print('Tente novamente')
            sleep(1.5)
            continue
        if op == '1':
            print('-' * 20, '\n')
            service = input('Qual o nome do serviço? -> ')
            username = input('Qual o nome de usuário? -> ')
            password = input('Qual a sua senha? -> ')
            nova_senha(service, username, password)
            print('-' * 20, '\n')
            input('PRESSIONE ENTER PARA CONTINUAR')

        if op == '2':
            print('-' * 20, '\n')
            mostrar_serviço()
            print('-' * 20, '\n')
            input('PRESSIONE ENTER PARA CONTINUAR')

        if op == '3':
            print('-' * 20, '\n')
            mostrar_serviço()
            service = input('De qual serviço você gostaria de recuperar a senha? -> ')
            obter_senha(service)
            print('-' * 20, '\n')
            input('PRESSIONE ENTER PARA CONTINUAR')

        if op == '4':
            render(choice(adeus))
            print('-' * 20)
            print('OBRIGADO POR USAR ESTE SERVIÇO!')
            print('   Created by: André Fernandes')
            print('-' * 20)
            input('PRESSIONE ENTER PARA CONTINUAR')
            break

c.close()
