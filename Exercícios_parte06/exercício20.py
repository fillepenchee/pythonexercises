
numero = 0
counter = 0
numpares = 0

while numero != 1000:
    numero = int(input('Digite um número: \n'))
    counter = counter + 1
    if numero % 2 == 0:
        numpares = numpares + 1

print(f'Foram digitados {counter} números, dos quais {numpares} são pares.')

