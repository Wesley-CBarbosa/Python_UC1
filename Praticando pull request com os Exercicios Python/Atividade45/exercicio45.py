# Exercício 45: Crie uma lista de números e remova os duplicados.

num = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

num_unicos = []

for x in num:
  if x not in num_unicos:
    num_unicos.append(x)

print(num_unicos)