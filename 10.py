"""
Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo
compreendido por eles.
"""

num1 = int(input("Digite um número: "))
num2 = 0

while num2 == 0:
    num2 = int(input("Digite outro número: "))
    if num2 == num1:
        print("Informe um valor diferente do primeiro número")
        num2 = 0
if num1 < num2:
    for v in range(num1, num2+1):
        print(v, end=' ')
else:
    for v in range(num2, num1+1):
        print(v, end=' ')