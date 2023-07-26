
salario = int(input('Digite o salário atual do funcionário: \n'))
tempo = int(input('Digite o tempo de serviço do funcionário em anos: \n'))
bonus = 0

if tempo < 1 and salario > 2000:
    print('O funcionário não recebeu nenhum aumento salarial.')

if salario <= 500:
    salario = salario + (salario * 0.25)
elif 500 < salario <= 1000:
    salario = salario + (salario * 0.2)
elif 1000 < salario <= 1500:
    salario = salario + (salario * 0.15)
elif 1500 < salario <= 2000:
    salario = salario + (salario * 0.1)

if 1 <= tempo <= 3:
    bonus = 100
elif 4 <= tempo <= 6:
    bonus = 200
elif 7 <= tempo <= 10:
    bonus = 300
elif tempo > 10:
    bonus = 500

salario = salario + bonus

print(f'O salário será de R$ {salario}.')
