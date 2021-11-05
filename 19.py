"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.

Altere o programa anterior para que ele aceite apenas números
entre 0 e 1000.
"""

qtos = int(input("Quantos número você quer informar? "))

menor = maior = soma = 0

for v in range(1, qtos+1):
    while True:
        num = int(input(f"Digite o {v}º número: "))
        if num < 0 or num > 1000:
            print('Digite um valor entre 0 e 1000!')
        else:
            break
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
