
prova1 = float(input('Nota da prova 1:'))
prova2 = float(input('Nota da prova 2:'))
prova3 = float(input('Nota da prova 3:'))
media = (prova1 + prova2 + (prova3 * 2)) / 4

print(media)
if media > 60.0:
    print('O(A) aluno(a) está aprovado(a).')
else:
    print('O(a) aluno(a) está reprovado(a).')
