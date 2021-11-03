"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
while True:
    try:
        num1 = int(input("Digite a base: "))
        num2 = int(input("Digite o expoente: "))

        exp = 1

        for v in range(0, num2):
            exp *= num1
    except ValueError:
        print('Informe um número inteiro!')
    else:
        print(f'A potência de {num1} elevado a {num2} é igual a {exp}.')
        break
