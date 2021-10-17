n, x, xpmin = input().split()
n = int(n)
x = int(x)
xpmin = int(xpmin)

for i in range(n):
  xp, q = input().split()
  xp = int(xp)
  q = int(q)

  if xp >= xpmin:
    print(xp + x, q + 1)
  else:
    print(xp, q)