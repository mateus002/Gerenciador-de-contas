import os
from getpass import getpass
from banco import cursor, conexao






def limpar():
    os.system('cls')
   
def cadastro():
    limpar()
    print('====Cadastro====')
    usuario = input('Usuário: ')
    senha = getpass('Senha: ')
    cursor.execute("INSERT INTO usuarios(usuario, senha) VALUES (?, ?)",
                   (usuario, senha))
    conexao.commit()

def login():
    limpar()
    print('====Login====')
    usuario = input('Usuário: ')
    senha = getpass('Senha: ')
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
                    (usuario, senha))
    
    resultado = cursor.fetchone()
    print(resultado)

    if resultado:
            print(f"Bem vindo ao sistema.{usuario}")
            
            
    else:
            print("usuário ou senha incorretos.")



def menu():
    # limpar()
    print('====Bem-vindo====')
    print('escolha uma opção \n' \
    '1-cadastro\n' \
    '2-login\n' \
    '3-sair')
    dig = input('=> ')
    if dig == '1':
        cadastro()
    elif dig == '2':
        login()
    elif dig == '3':
        return False
    
    return True

while menu():
     pass

  