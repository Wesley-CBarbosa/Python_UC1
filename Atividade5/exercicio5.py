# Exercício 5: Peça três números e exiba o maior.

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("informe o segundo valor: "))
num3 = int(input("Informe o terceiro valor: "))

if num1 > num2 and num3:
  print("O primeiro valor é o maior.")
elif num2 > num1 and num3:
  print("O segundo número é o maior.")
elif num3 > num1 and num2:
  print("O terceiro número é o maior.")
else:
  print("Todos os valores tem o mesmo valor.]")