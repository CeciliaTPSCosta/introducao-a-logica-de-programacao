X = int(input())
Y = int(input())

if X == 0 and Y == 0:
  print('Centro')
if X > 0 and Y > 0:
  print('Quadrante 1')
if X < 0 and Y > 0:
  print('Quadrante 2')
if X > 0 and Y < 0:
  print('Quadrante 4')
if X < 0 and Y < 0:
  print('Quadrante 3')
