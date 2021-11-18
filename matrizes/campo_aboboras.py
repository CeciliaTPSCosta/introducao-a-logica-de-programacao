tamanho_plantacao = int(input())
plantacao = []

for abobora in range(tamanho_plantacao):
    pesos = [int(x) for x in input().split()]
    plantacao.append(pesos)

linha_harry, coluna_ron = input().split()
linha_harry = int(linha_harry)
coluna_ron = int(coluna_ron)

ron = 0
harry = 0

for iterator in range(tamanho_plantacao):
    ron += plantacao[iterator][coluna_ron]
    plantacao[iterator][coluna_ron] = 0
    harry += plantacao[linha_harry][iterator]
    plantacao[linha_harry][iterator] = 0


print(f'Harry {harry}\nRon {ron}')