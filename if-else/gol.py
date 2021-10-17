zag, gol = input().split()
ata, chut = input().split()

if zag == ata:
  print('Driblado')
  if gol == chut:
    print('Gol')
  else:
    print('...e o goleiro pega')
else:
  print('Bloqueado')