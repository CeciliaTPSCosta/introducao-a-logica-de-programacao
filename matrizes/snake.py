linhas, colunas = input().split()
linhas = int(linhas)
colunas = int(colunas)
mapa = []

for i in range(linhas):
    linhas_mapa = [int(x) for x in input().split()]
    mapa.append(linhas_mapa)

pontos = 0

for i in range(linhas):
    for j in range(colunas):
        pontos += mapa[i][j]
        if pontos < 0:
            pontos = 0    
 
print(pontos)
        
        

