resistencia, poder = input().split()
resistencia = int(resistencia)
poder = int(poder)

somaataques = 0

while poder > 0 and resistencia > 0:
  resistencia -= poder
  poder -= 1
  somaataques += 1
  
if resistencia <= 0:
  print(somaataques)
else: 
  print('F')