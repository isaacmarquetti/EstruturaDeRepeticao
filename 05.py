"""
Supondo que a população de um país A seja da ordem de
80000 habitantes com uma taxa anual de crescimento de
3% e que a população de B seja 200000 habitantes com
uma taxa de crescimento de 1.5%. Faça um programa que
calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do
país B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação
"""

pais_a = taxa_a = pais_b = taxa_b = ano = 0

while pais_a <= 0:
    pais_a = int(input("Digite a população do país A: "))
    if pais_a <= 0:
        print("Informe um valor positivo.")

while taxa_a <= 0:
    taxa_a = float(input("Digite a taxa de crescimento do país A (%): "))
    if taxa_a <= 0:
        print("Informe uma taxa positiva.")

while pais_b == 0:
    pais_b = int(input("Digite a população do país B: "))
    if pais_b < pais_a or pais_b == pais_a:
        print("Informe uma população MAIOR que o país A")
        pais_b = 0

while taxa_b == 0:
    taxa_b = float(input("Digite a taxa de crescimento do país B (%): "))
    if taxa_b > taxa_a or taxa_b == taxa_a:
        print("Informe uma taxa MENOR que do país A")
        taxa_b = 0
    elif taxa_b < 0:
        print("Informe uma taxa positiva.")
        taxa_b = 0

while pais_a <= pais_b:
    cresc_a = pais_a * (taxa_a / 100)
    cresc_b = pais_b * (taxa_b / 100)
    pais_a += cresc_a
    pais_b += cresc_b
    ano += 1

print(f"Serão necessários {ano} anos para que o país A ultrapasse o país B.")

