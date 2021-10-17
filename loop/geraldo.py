n, m = input().split()
n = int(n)
m = int(m)

stronger = 0
poder = 0

for i in range(n):
    poder = 0
    p = input().split()

    for j in p:
        poder += int(j)
        if poder > stronger:
            stronger = poder
    
print(stronger)