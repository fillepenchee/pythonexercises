
num1 = int(input('Digite um número: \n'))
num2 = 0
print(f'O primeiro múltiplo de 11, 13 ou 17 após {num1} ')

while num2 == 0:
    num1 = num1 + 1
    if num1 % 11 == 0:
        num2 = num1
        print(f'é {num2}, múltiplo de 11.')
        break
    elif num1 % 13 == 0:
        num2 = num1
        print(f'é {num2}, múltiplo de 13.')
        break
    elif num1 % 17 == 0:
        num2 = num1
        print(f'é {num2}, múltiplo de 17.')
        break
