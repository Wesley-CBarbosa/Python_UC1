# Exercício 49: Percorra um dicionário e imprima suas chaves e valores.

pessoas = {'João': 30, 'Maria': 25, 'Pedro': 35, 'Ana': 28, 'Carlos': 40}

for nome, idade in pessoas.items():
  print(f"Nome: {nome}, Idade: {idade}")