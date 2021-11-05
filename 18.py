"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
"""

qtos = int(input("Quantos número você quer informar? "))

menor = maior = soma = 0

for v in range(1, qtos+1):
    num = int(input(f"Digite o {v}º número: "))
    soma += num
    if v == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')
print(f'Soma: {soma}')


