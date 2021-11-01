secoes = int(input())

comprimentos = input().split()
soma = 0

comprimento = [int(x) for x in comprimentos]
soma_todos = sum(comprimento) / 2

for secao in range(len(comprimento)):
    if soma < soma_todos:
        soma += comprimento[secao]
        final = secao + 1
        
print(final)
