frenetico = int(input())
pixels = []

for linha in range(10):
    pixel = [int(x) for x in input().split()]
    pixels.append(pixel)

for valores in pixels:
    for i in valores:
        if i == frenetico:
            print('sim')
            exit()
        else:
            nao = 'nao'

print(nao)