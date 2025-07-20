# Exercício 11: Crie um menu onde o usuário pode escolher entre somar, subtrair, multiplicar e dividir dois números.

operacao = str(input("A conta que quer realizar é de somar, subtrair, multiplicar ou dividir? "))
a = int(input("Informe primeiro valor: "))
b = int(input("Informe segundo valor: "))

def calculadora (a, b, op):

  if op == "somar":
    return a + b
  elif op == "subtrair":
    return a - b
  elif op == "multiplicar":
    return a * b
  elif op == "dividir":
    return a / b
  else:
    print("Operação inválida.")

resultado=(calculadora (a, b, operacao))
print("Resultado:", resultado)