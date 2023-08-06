
impar = int(input('Digite um número ímpar: \n'))
counter = 1

while (impar % 2) == 0:
    impar = int(input('O número digitado é par. Favor digitar um ímpar:\n'))

while counter <= impar:
    print(counter)
    counter = counter + 2
