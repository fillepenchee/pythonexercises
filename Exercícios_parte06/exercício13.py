
par = int(input('Digite um número par: \n'))
counter = 0

while (par % 2) == 1:
    par = int(input('O número digitado é ímpar. Favor digitar um par:\n'))

while counter <= par:
    print(counter)
    counter = counter + 2
