
numero = int(input('Digite um número entre 100 e 999: \n'))

while numero not in range(100, 999):
    numero = int(input('O número digitado está fora do intervalo 100-999. Digite um'
                       'que esteja no intervalo 100-999: \n'))

for i in str(numero):
    print(i)
