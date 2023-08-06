
qtdenum = int(input('Digite a quantidade de números a ser inserida: \n'))
numeromaior = 0
count = 0
vezes = 0

while count < qtdenum:
    novonum = int(input('Digite um número: \n'))
    count = count + 1
    if novonum > numeromaior:
        numeromaior = novonum
        vezes = 0
    if novonum == numeromaior:
        vezes = vezes + 1

print(f'O maior número digitado é {numeromaior}, que apareceu {vezes} vez(es).')
