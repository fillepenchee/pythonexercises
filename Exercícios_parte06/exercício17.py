
numero = int(input('Digite um número inteiro positivo: \n'))
counter = 0

while numero < 0:
    numero = int(input('O número digitado não é positivo. Favor inserir um positivo: \n'))

while counter <= numero:
    print(counter)
    counter = counter + 1
