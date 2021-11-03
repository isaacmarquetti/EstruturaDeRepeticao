"""
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
"""

nome_usuario = ''
senha = ''

while senha == nome_usuario:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha == nome_usuario:
        print("Nome e senha são iguais! Digite novamente.")
    else:
        print("Usuário cadastrado.")