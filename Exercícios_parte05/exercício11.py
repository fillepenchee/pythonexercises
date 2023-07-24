
numero = int(input('Digite um número maior que zero:'))
soma = 0

if numero > 0:
    for i in str(numero):
        soma = int(i) + soma
    print(soma)
if numero <= 0:
    print('Número inválido.')
