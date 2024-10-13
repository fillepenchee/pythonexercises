
n = 0
pos = 1
minha_lista = []
while n < 11:
    minha_lista.append(int(input("Digite um número: \n")))
    n += 1
maior = minha_lista[0]
menor = minha_lista[0]
while pos < len(minha_lista):
    if minha_lista[pos] > maior:
        maior = minha_lista[pos]
    if minha_lista[pos] < menor:
        menor = minha_lista[pos]
    pos += 1

print(f"Os números fornecidos foram {minha_lista}. O maior deles é {maior} e o menor deles é {menor}.")
