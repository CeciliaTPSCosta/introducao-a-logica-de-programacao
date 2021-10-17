todos = map(int, input().split())
pares = []

for n in todos:
    if n % 2 == 0:
        pares.append(n)

print(pares)