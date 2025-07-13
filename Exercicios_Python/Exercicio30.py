# Exercício 30: Crie um programa que peça 5 números e exiba apenas os números pares.

print("Digite 5 números e veja somente os pares.")

numeros = []

for i in range(5):
    n = int(input(f"\nDigite o {i+1}º número: "))
    numeros.append(n)

print("\nNúmeros pares digitados:")
for x in numeros:
    if x % 2 == 0:
        print(x)
