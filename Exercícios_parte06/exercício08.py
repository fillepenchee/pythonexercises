
counter = 0
maior = 0
menor = 0

while counter in range(0, 10):
    valor = int(input('Digite um valor inteiro: \n'))
    counter = counter + 1
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'O maior valor digitado é {maior} e o menor valor digitado é {menor}.')
