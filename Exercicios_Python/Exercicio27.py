# Exercício 27: Crie um programa que peça um número e imprima sua contagem regressiva até 0.

n = int(input("Digite um número e veja a sua contagem regressiva: "))

for x in range(n, 0, -1):
  print(x)