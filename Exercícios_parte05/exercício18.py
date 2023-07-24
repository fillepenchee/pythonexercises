
operacao = int(input('Digite o número para escolher sua operação matemática: \n 1-Soma \n 2-Subtração \n'
      '3-Multiplicação \n 4-Divisão \n'))

while 1 > operacao or operacao > 4:
    print('Valor não reconhecido, favor digitar outro')
    operacao = int(input('Digite o número para escolher sua operação matemática: \n 1-Soma \n 2-Subtração \n'
                         '3-Multiplicação \n 4-Divisão \n'))

num1 = float(input('Agora digite um número com que fazer a operação: \n'))
num2 = float(input('Agora digite outro número: \n'))


if operacao == 1:
    print(f'O resultado é {num1 + num2}.')
elif operacao == 2:
    print(f'O resultado é {num1 - num2}.')
elif operacao == 3:
    print(f'O resultado é {num1 * num2}.')
elif operacao == 4:
    print(f'O resultado é {num1 / num2}.')

