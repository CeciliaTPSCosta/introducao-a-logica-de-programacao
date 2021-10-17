xEntrega, yEntrega = input().split()
xDrone, yDrone = input().split()
xEntrega = int(xEntrega)
yEntrega = int(yEntrega)
xDrone = int(xDrone)
yDrone = int(yDrone)

if xEntrega == xDrone and yEntrega == yDrone:
  print('Soltar pacote')
else:
  print('Nao soltar pacote')