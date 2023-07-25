
nota = float(input('Digite a nota final do aluno: \n'))
faltas = float(input('Digite quantas faltas o aluno teve: \n'))

if 9.0 < nota < 10.0:
    if faltas < 20:
        print(f'O conceito final do aluno é A')
    else:
        print(f'O conceito final do aluno é B')
if 7.5 < nota < 8.9:
    if faltas < 20:
        print(f'O conceito final do aluno é B')
    else:
        print(f'O conceito final do aluno é C')
if 5.0 < nota < 7.4:
    if faltas < 20:
        print(f'O conceito final do aluno é C')
    else:
        print(f'O conceito final do aluno é D')
if 4.0 < nota < 4.9:
    if faltas < 20:
        print(f'O conceito final do aluno é D')
    else:
        print(f'O conceito final do aluno é E')
if 0.0 < nota < 3.9:
    if faltas < 20:
        print(f'O conceito final do aluno é E')
    else:
        print(f'O conceito final do aluno é E')