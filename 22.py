"""
Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo,
por quais número ele é divisível.
"""
"""
Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.
"""

num = int(input("Digite um número: "))
cont = (num + 1) / 2
primo = True

for i in range(2, int(cont)):
    if num % i == 0:
        primo = False

if primo:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
    print(f'Pode ser divisível por:')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end='; ')

