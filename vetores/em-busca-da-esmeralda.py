caixas = int(input())

numDaEsmeralda = input().split()
esm = [int(n) for n in numDaEsmeralda]

esmDoMal = int(input())

for i in range(caixas):
    if esm[i] == esmDoMal:
        print(esmDoMal) 
        exit()
        
print(-1)