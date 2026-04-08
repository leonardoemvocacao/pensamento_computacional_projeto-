# 1. Definimos a função com o nome 'saudar'
# O que está entre parênteses (nome) é chamado de PARÂMETRO
def saudar(nome):
    """
    Esta função recebe um nome e exibe uma saudação.
    """
    print(f"Olá, {nome}! Bem-vindo ao mundo da programação.")

# 2. Chamamos (executamos) a função
# Passamos o valor "Tiago" para dentro do parâmetro 'nome'
saudar("Tiago")
saudar("Maria")

# Definimos a função para organizar o processo de login
def realizar_login():
    """
    Função que simula uma tela de login capturando nome e senha.
    """
    print('\n--- Tela de login - Meet ---')
    
    # Captura de dados (como no teu exemplo original)
    nome_usuario = input('Digite seu login para continuar: ')
    senha_usuario = input('Digite sua senha para continuar: ')
    
    # Exibe a mensagem de sucesso
    print(f'Bem-vindo, {nome_usuario}!')
    print('---------------------------\n')

# Agora, para o código funcionar, precisamos "CHAMAR" a função:
realizar_login()

import getpass  # Importamos a biblioteca de segurança

def realizar_login_invisivel():
    """
    Função de login que esconde os caracteres da senha ao digitar.
    """
    senha_padrao = "vocacao2025"
    
    print('\n--- Sistema de Login Protegido ---')
    nome_usuario = input('Digite seu login: ')
    
    # getpass faz com que o que é digitado não apareça no ecrã
    senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

    if senha_digitada == senha_padrao:
        print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
    else:
        print('\n[ERRO] Senha incorreta!')
    
    print('----------------------------------\n')

# Executar a função
realizar_login_invisivel()


import getpass

def realizar_login_com_tentativas():
    """
    Função de login que permite até 3 tentativas antes de bloquear.
    """
    senha_padrao = "vocacao2025"
    tentativas_restante = 3
    login_sucesso = False 

    print('\n--- Sistema de login (Máx 3 Tentativas)---')
    nome_usuario = input('Digite seu login:')

    while tentativas_restante > 0 and not login_sucesso:
        print(f'\nTentativas restantes: {tentativas_restante}')