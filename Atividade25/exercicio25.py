# Exercício 25: Imprima os 10 primeiros números da sequência de Fibonacci.

n = int(input("Quantos números da sequência de Fibonacci você deseja? "))
fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print(fibonacci[:n])