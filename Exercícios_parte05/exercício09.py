
salario = float(input('Digite o valor do salário:'))
prestacao = float(input('Digite o valor da prestação:'))

if prestacao < (salario * 0.2):
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado. Escolha um valor de prestação menor.')
