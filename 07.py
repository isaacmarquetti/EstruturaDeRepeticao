"""
Faça um programa que leia 5 números e informe o maior número.
"""

maior = 0

for v in range(1, 6):
    num = int(input(f"Digite o {v}º numero: "))

    if num > maior:
        maior = num

print(f'O maior valor digitado foi o número {maior}.')