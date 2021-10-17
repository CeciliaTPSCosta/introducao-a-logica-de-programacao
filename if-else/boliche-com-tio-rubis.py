qPistas, pessoasporPista, alunos = input().split()
qPistas = int(qPistas) 
pessoasporPista = int(pessoasporPista)
alunos = int(alunos) 

total = float((alunos + 1) / qPistas)

if total <= pessoasporPista:
  print('S')
else:
  print('N')
