
import random as random

contagem = 0

a = int(random.choice(range(1, 100)))
b = int(random.choice(range(1, 100)))
resp1 = int(a + b)

aluno1 = int(input(f'Qual é a soma de {a} + {b}?'))
if aluno1 == resp1:
    contagem = contagem + 1

c = int(random.choice(range(1, 100)))
d = int(random.choice(range(1, 100)))
resp2 = int(c + d)

aluno2 = int(input(f'Qual é a soma de {c} + {d}?'))
if aluno2 == resp2:
    contagem = contagem + 1

e = int(random.choice(range(1, 100)))
f = int(random.choice(range(1, 100)))
resp3 = int(e + f)

aluno3 = int(input(f'Qual é a soma de {e} + {f}?'))
if aluno3 == resp3:
    contagem = contagem + 1

g = int(random.choice(range(1, 100)))
h = int(random.choice(range(1, 100)))
resp4 = int(g + h)

aluno4 = int(input(f'Qual é a soma de {g} + {h}?'))
if aluno4 == resp4:
    contagem = contagem + 1

i = int(random.choice(range(1, 100)))
j = int(random.choice(range(1, 100)))
resp5 = int(i + j)

aluno5 = int(input(f'Qual é a soma de {i} + {j}?'))
if aluno5 == resp5:
    contagem = contagem + 1

print(f'Pergunta 1: {a} + {b} = {resp1}. Sua resposta foi {aluno1}.\n')
print(f'Pergunta 2: {c} + {d} = {resp2}. Sua resposta foi {aluno2}.\n')
print(f'Pergunta 1: {e} + {f} = {resp3}. Sua resposta foi {aluno3}.\n')
print(f'Pergunta 1: {g} + {h} = {resp4}. Sua resposta foi {aluno4}.\n')
print(f'Pergunta 1: {i} + {j} = {resp5}. Sua resposta foi {aluno5}.\n')
print(f'Você acertou {contagem} de 5 perguntas.')
