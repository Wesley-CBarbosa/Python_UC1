## Exercício 37: Crie uma lista e inverta a ordem dos elementos.

lista = [1, 2, 3, 4, 5]
lista_invertida = []

for x in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[x])

print(lista_invertida)