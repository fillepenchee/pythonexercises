
par = int(input('Digite um número par: \n'))

while (par % 2) == 1:
    par = int(input('O número digitado é ímpar. Favor digitar um par:\n'))

while par >= 0:
    print(par)
    par = par - 2
