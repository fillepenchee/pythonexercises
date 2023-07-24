
nota1 = float(input('Digite a nota 01 do aluno(a):'))
nota2 = float(input('Digite a nota 02 do aluno(a):'))

if (nota1 > 0) and (nota1 < 10.0) and (nota2 > 0) and (nota2 < 10.0):
    print((nota1 + nota2) / 2)
else:
    print('Um ou ambos os números digitados não é(são) válido(s).')
