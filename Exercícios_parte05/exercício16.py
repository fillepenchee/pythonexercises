
diames = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
          'julho', 'agosto', 'setembro', 'outubro', 'novembro',
          'dezembro']

dianum = int(input('Digite o número do mês: \n'))

if 1 < dianum > 12:
    print('Este não é um número de mês válido.')
else:
    print(f'Estamos em {diames[dianum - 1]}.')
