
inteiro = int(input('Digite um número inteiro: \n'))

while inteiro in range(0, 100000):
    print(inteiro)
    inteiro = inteiro + 1000
else:
    print(100000)
