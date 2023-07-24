dia_sem = ['domingo', 'segunda', 'terça', 'quarta',
           'quinta', 'sextou', 'sábado']

dia_num = int(input('Digite o dia da semana:'))

if 1 < dia_num > 7:
    print('Esse dia não existe.')
else:
    print(f'Estamos na(o) {dia_sem[dia_num - 1]}.')
