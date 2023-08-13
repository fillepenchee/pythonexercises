
num1 = int(input('Digite um número: \n'))
num2 = int(input('Digite um número maior que o anterior: \n'))
soma = 0
multiplic = 1

while num2 <= num1:
    num2 = int(input(f'O número digitado não é maior que o primeiro, {num1}.'
                     'Favor digitar um maior: \n'))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma = soma + i
    elif i % 2 != 0:
        multiplic = multiplic * i

print(f'A soma dos números pares no intervalo é {soma}, e a multiplicação dos \n'
      f'números ímpares no intervalo é {multiplic}.')
