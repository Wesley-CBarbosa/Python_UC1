# Exercício 36: Crie uma lista com 5 números e imprima o maior.

num = [1, 2, 3, 4, 5]

maior = num[0]

for x in num:
  if x > maior:
    maior = x

print(maior)