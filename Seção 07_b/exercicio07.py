
n = 0
pos = 1
minha_lista = []
while n < 10:
    minha_lista.append(int(input("Digite um número: \n")))
    n += 1
maior = minha_lista[0]
posicao_maior = pos
while pos < len(minha_lista):
    if minha_lista[pos] > maior:
        maior = minha_lista[pos]
        posicao_maior = (pos - 1)
    pos += 1

print(f"Os números fornecidos foram {minha_lista}. O maior deles é {maior} e ele está na {posicao_maior}a. posição.")
