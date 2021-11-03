"""
Faça um programa que leia 5 números e informe
a soma e a média dos números.
"""

soma = 0
cont = 0

for v in range(1, 6):
    num = int(input(f"Digite o {v}º numero: "))
    soma += num
    cont += 1

media = soma / cont

print(f'Soma: {soma}')
print(f'Média: {media:.1f}')