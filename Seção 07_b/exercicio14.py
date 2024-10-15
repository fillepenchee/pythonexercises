from collections import defaultdict

minha_lista = []
n = 0

while n < 10:
    a = (float(input(f"Digite um número: \n")))
    if not isinstance(a, (int, float)):
        a = (float(input("O número não é válido. Favor digitar um número: \n")))
    minha_lista.append(a)
    n += 1

print(minha_lista)

u = 0
lista2 = []
lista_repetidos = []
while u < len(minha_lista):
    if minha_lista[u] in lista2:
        lista_repetidos.append(minha_lista[u])
    else:
        lista2.append(minha_lista[u])
    u += 1


print(f"Foram digitados {len(lista_repetidos)} valores repetidos: {lista_repetidos}.")
