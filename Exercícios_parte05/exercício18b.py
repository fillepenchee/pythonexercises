
# Seção 05 Exercício 18
# solução do Fellipe em
# https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/learn/lecture/11892764#questions/11377448

condicao = int(input("[1] - adição \n [2] - subtração\n [3] - multiplicação\n [4] - divisão\n"
                     "Escolha uma opção para realizar uma operação matemática:"))

while condicao < 1 or condicao > 4:
    print("Valor não reconhecido, favor inserir um número inteiro entre 1 e 4.")
    condicao = int(input("[1] - adição \n [2] - subtração\n [3] - multiplicação\n [4] - divisão\n"
                         "Escolha uma opção para realizar uma operação matemática:"))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if condicao == 1:
    soma = num1 + num2
    print("A função escolhida foi adição e {0} + {1} = {2}".format(num1, num2, soma))
elif condicao == 2:
    subtracao = num1 - num2
    print("A função escolhida foi subtração e {0} - {1} = {2}".format(num1, num2, subtracao))
elif condicao == 3:
    multi = num1 * num2
    print("A função escolhida foi multiplicação e {0} x {1} = {2}".format(num1, num2, multi))
elif condicao == 4:
    divisao = num1 / num2
    print("A função escolhida foi divisão e {0} / {1} = {2}".format(num1, num2, divisao))
else:
    print("Operação inválida")