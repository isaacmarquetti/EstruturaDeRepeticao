"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""
nome = sexo = estado_civil = ''
idade = salario = -1

while len(nome) < 3:
    nome = input("Digite seu primeiro nome: ")
    if len(nome) < 3:
        print('Digite um nome válido.')
    else:
        print('Nome cadastrado com sucesso!')

while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 150:
        print('Digite uma idade válida.')
    else:
        print("Idade cadastrada com sucesso!")

while salario < 0:
    salario = float(input("Digite seu salário: R$"))
    if salario < 0:
        print("Digite um salário válido.")
    else:
        print("Salário cadastrado com sucesso!")

while sexo == '':
    sexo = input("Digite seu sexo (M/F): ").upper()
    if sexo == 'M' or sexo == 'F':
        print('Sexo cadastrado com sucesso!')
    else:
        print('Digite um sexo válido.')
        sexo = ''

while estado_civil == '':
    estado_civil = input("Digite o seu estado civil: ").upper()
    if estado_civil == 'C' or estado_civil == 'S' or estado_civil == 'V' or estado_civil == 'D':
        print("Estado civil cadastrado com sucesso!")
    else:
        print('Digite um estado civil válido.')
        estado_civil = ''
