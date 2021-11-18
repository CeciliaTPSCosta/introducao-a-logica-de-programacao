frenetico = int(input())
linhas = 10

pixels = []

for linha in range(linhas):
    pixel = [int(x) for x in input().split()]
    pixels.append(pixel)

for valores in pixels:
    for i in valores:
        if i == frenetico:
            print('sim')
            exit()
        else:
            sim_ou_nao = 'nao'

print(sim_ou_nao)