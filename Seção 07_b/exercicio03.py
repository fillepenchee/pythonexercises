
lista1 = []
lista2 = []
contador = 0

while contador < 10:
    numero = int(input("Digite o valor desejado: \n"))
    lista1.append(numero)
    lista2.append(numero**2)
    contador += 1

print(lista1)
print(lista2)
