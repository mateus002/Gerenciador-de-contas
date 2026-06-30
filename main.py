import os
from getpass import getpass

def limpar():
    os.system('cls')

def menu():
    limpar()
    print('====Bem-vindo====')
    print('escolha uma opção \n' \
    '1-cadastro\n' \
    '2-login')
    dig = input('=> ')
    if dig == '1':
        cadastro()
    elif dig == '2':
        login()
    
    ...

def login():
  limpar()
  print('====Login====')
  input('Usuário: ')
  senha = getpass('Senha: ')
  

def cadastro():
    limpar()
    print('====Cadastro====')
    input('Nome: ')
    input('Usuário: ')
    senha = getpass('Senha: ')

    ...

menu()