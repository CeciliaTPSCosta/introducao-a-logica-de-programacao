dimensao, teleportes = input().split()
dimensao = int(dimensao)
teleportes = int(teleportes)

mapinha = []

for quadrantes in range(dimensao):
    quadrante = [int(x) for x in input().split()]
    mapinha.append(quadrante)

abatidas = 0
for este_caralho in range(teleportes):
    dimx, dimy = input().split()
    dimx, dimy = int(dimx), int(dimy)
    for i in range(dimx, -1, -1):
        if mapinha[i][dimy] == 1:
            abatidas += 1
            mapinha[i][dimy] = 0
            break

print(abatidas)












# for i in range(len(mapinha)):
    # for j in range(len(mapinha)):

































#for location in range(teleportes):
    #dimx, dimy = [int(x) for x in input().split()]
    
    #print(mapinha[dimx][dimy])
    

# mapinha[dimx][dimy] -> location on the little map skoaksaok 



