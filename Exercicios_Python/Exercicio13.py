# Exercício 13: Crie um programa que traduza números de 1 a 5 para palavras (1 = um, 2 = dois...).

print("Informe um número de 1 à 5 e veja ele por extenso")
operacao = int(input("\nInforme um valor: \n"))

def numero (op):

  if op == 1:
    print("Um")
  elif op == 2:
    print("Dois")
  elif op == 3:
    print("Três")
  elif op == 4:
    print("Quatro")
  elif op == 5:
    print("Cinco")
  else:
    print("O valor informado não se enquadra na condição proposta.")

resultado = (numero (operacao))
