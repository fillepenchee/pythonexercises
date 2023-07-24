
operacao = int(input('Escolha a opção: \n 1- Soma de 2 números \n 2- Diferença entre 2 números (maior'
                     'pelo menor)\n'
                     '3- Produto entre 2 números \n 4- Divisão entre 2 números (o denominador não'
                     'pode ser zero) \n Opção: '))

while 1 < operacao > 4:
    print('Opção inválida, digite um número de 1 a 4:')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while operacao == 4 and num2 == 0:
    print('O denominador não pode ser zero, favor digitar outro')
    num2 = int(input('Digite o segundo número: '))

if operacao == 1:
    print(num1 + num2)

if operacao == 2:
    if num1 > num2:
        print(num1 - num2)
    if num2 > num1:
        print(num2 - num1)

if operacao == 3:
    print(num1 * num2)

if operacao == 4:
    print(num1 / num2)
