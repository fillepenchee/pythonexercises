
prova1 = float(input('Nota do trabalho de laboratório:'))
prova2 = float(input('Nota da avaliação semestral:'))
prova3 = float(input('Nota do exame final:'))
media = ((prova1 * 2) + (prova2 * 3) + (prova3 * 5)) / 10

print(media)
if media < 2.9:
    print('O(A) aluno(a) está reprovado(a).')
elif media > 3 and media < 4.9:
    print('O(A) aluno(a) está de recuperação.')
else:
    print('O(a) aluno(a) está aprovado(a).')
