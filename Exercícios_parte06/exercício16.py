
impar = int(input('Digite um número ímpar: \n'))

while (impar % 2) == 0:
    impar = int(input('O número digitado é par. Favor digitar um ímpar:\n'))

    while impar >= 1:
        print(impar)
        impar = impar - 2
