
data = input('Digite uma data de nascimento (dd/mm/aaaa): \n')

dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
validames = 0
validadia = 0

if 1 <= mes <= 12:
    validames = 1

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        validadia = 1
elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        if 1 <= dia <= 29:
            validadia = 1
    elif 1 <= dia <= 28:
        validadia = 1
else:
    if 1 <= dia <= 30:
        validadia = 1

if validadia == 1 and validames == 1:
    print(f'A data de {dia}/{mes}/{ano} é válida.')
else:
    print('A data digitada é inválida.')
