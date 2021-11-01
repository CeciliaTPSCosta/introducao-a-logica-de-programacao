qtdFases = int(input())

caminhos = input().split()
fase = [int(n) for n in caminhos]

hp = int(input())
contadorHp = 0

for i in range(qtdFases):
    if fase[i] == 1:
        contadorHp = 0
        contadorHp += hp
    if fase[i] != 0 and fase[i]!= 1:
        contadorHp = contadorHp - fase[i]
        if contadorHp <= 0:
            print('You Died')
            exit()

print('Yes, you can')
