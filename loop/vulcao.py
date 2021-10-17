t = int(input())
p = int(input())

i = 0

while p != 0:
  if p <= t:
    i = i
  else:
    i = p
  p = int(input())

if i > t:
  print('ALARME')
else: 
  print('O Havai pode dormir tranquilo')