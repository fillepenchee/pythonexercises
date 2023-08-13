
num1 = int(input('Digite um número positivo: \n'))
i = 1
lista1 = []

while num1 <= 0:
    num1 = int(input('O número digitado é negativo ou zero. Favor digitar'
                     ' um número positivo: \n'))

while i <= num1:
    if num1 % i == 0:
        lista1.append(i)
        i = i + 1
    else:
        i = i + 1

print(f'O número {num1} tem os seguintes divisores inteiros: {lista1}.')
