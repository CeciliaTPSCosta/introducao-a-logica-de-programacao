N1, N2, N3, N4, N5, N6 = input().split()
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
N4 = int(N4)
N5 = int(N5)
N6 = int(N6)

soma = N1 + N2 + N3 + N4 + N5 + N6

if soma >= 250:
  print('S+')
elif soma >= 200:
  print('S')
elif soma >= 180:
  print('S-')
elif soma >= 150:
  print('A+')
elif soma >= 100:
  print('A')
elif soma >= 80:
  print('A-')
elif soma >= 60:
  print('B+')
elif soma >= 40:
  print('B')
else:
  print('B-')