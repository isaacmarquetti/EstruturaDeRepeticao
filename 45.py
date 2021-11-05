"""
Desenvolver um programa para verificar a nota do aluno em uma
prova com 10 questões, o programa deve perguntar ao aluno a
resposta de cada questão e ao final comparar com o gabarito
da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa).

Após cada aluno utilizar o sistema deve ser feita uma pergunta
se outro aluno vai utilizar o sistema.

Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.

    Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A

    Após concluir isto você poderia incrementar o programa permitindo
     que o professor digite o gabarito da prova antes dos
     alunos usarem o programa.
"""

print(" ### GABARITO DA PROVA ### ")

soma_nota = alunos = maior = menor = 0

while True:
    print("Digite o gabarito da prova: ")
    nota = 0
    for v in range(1, 11):
        gabarito = input(f"Questão {v}: ").upper()
        if v == 1:
            if gabarito == 'A':
                nota += 1
        if v == 2:
            if gabarito == 'B':
                nota += 1
        if v == 3:
            if gabarito == 'C':
                nota += 1
        if v == 4:
            if gabarito == 'D':
                nota += 1
        if v == 5:
            if gabarito == 'E':
                nota += 1
        if v == 6:
            if gabarito == 'E':
                nota += 1
        if v == 7:
            if gabarito == 'D':
                nota += 1
        if v == 8:
            if gabarito == 'C':
                nota += 1
        if v == 9:
            if gabarito == 'B':
                nota += 1
        if v == 10:
            if gabarito == 'A':
                nota += 1
    soma_nota += nota
    alunos += 1
    print(f'Nota: {nota:.2f}')

    if alunos == 1:
        maior = nota
        menor = nota

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

    sair = input("Deseja continuar (S/N): ").upper()
    if sair == 'N':
        break

media = soma_nota / alunos
print(f'Maior nota: {maior:.2f}')
print(f'Menor nota: {menor:.2f}')
print(f'Total de alunos: {alunos}')
print(f'Média: {media:.2f}')