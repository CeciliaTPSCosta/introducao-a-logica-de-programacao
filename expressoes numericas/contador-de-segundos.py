segundosTotais = input()
segundosTotais = int(segundosTotais)
h = segundosTotais // 60 // 60
min = (segundosTotais // 60) - h * 60
s = segundosTotais % 60
print('{}h {}m {}s'.format(h, min, s))