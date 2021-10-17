LC, O, L, AC = input().split()
LC = int(LC)
O = int(O)
L = int(L)
AC = int(AC)

LC = LC // 4
O = O // 8
L = L // 2
AC = AC // 1

if LC <= O and LC <= L and LC <= AC:
  tempo = LC * 1259

if O <= LC and O <= L and O <= AC:
  tempo = O * 1259

if L <= LC and L <= O and L <= AC:
  tempo = L * 1259

if AC <= LC and AC <= O and AC <= L:
  tempo = AC * 1259

h = tempo // 60 // 60
min = (tempo // 60) - h * 60
s = tempo % 60

print('{} h {} m {} s'.format(h, min, s))