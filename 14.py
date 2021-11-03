"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a
quantidade de números impares.
"""

cont_par = 0
cont_impar = 0
for v in range(0, 10):
    num = int(input(f"Digite o {v+1}º número inteiro: "))

    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'Números de pares: {cont_par}')
print(f'Números de ímpares: {cont_impar}')