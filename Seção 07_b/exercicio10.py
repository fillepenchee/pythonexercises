
minha_lista = []
n = 0
soma = 0
while n < 15:
    a = (float(input(f"Digite a nota do {n + 1}o aluno: \n")))
    if not isinstance(a, (int, float)):
        a = (float(input("A nota não é válida. Favor digitar um número: \n")))
    minha_lista.append(a)
    soma = soma + a
    n += 1

print(f"As notas dos alunos foram {minha_lista} e a média geral foi de {soma / 15}.")
