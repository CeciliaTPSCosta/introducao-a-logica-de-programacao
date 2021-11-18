dim1, dim2 = input().split()
dim1 = int(dim1)
dim2 = int(dim2)

valores_m1 = []
valores_m2 = []

# pegando a matriz A 
for linha in range(dim1):
    m1 = [int(x) for x in input().split()]
    valores_m1.append(m1)

# pegando a matriz B
for linha in range(dim1):
    m2 = [int(x) for x in input().split()]
    valores_m2.append(m2)

resultado = []
# percorrendo e subtraindo
for i in range(dim1):
    valores_m3 = []
    for j in range(dim2):   
        matriz_c = valores_m1[i][j] - valores_m2[i][j]
        valores_m3.append(matriz_c)
    resultado.append(valores_m3)

for i in resultado:
    print(*i)