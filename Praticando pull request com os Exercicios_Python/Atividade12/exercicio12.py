# Exercício 12: Crie um menu para converter temperaturas entre Celsius, Fahrenheit e Kelvin.

print("Informe qual o tipo de converção deseja realizar escolhendo a letra da operação.")
print("\nA.Celsius p/ Fahrenheit \nB.Celsius p/ Kelvin \nC.Fahrenheit p/ Celsius \nD.Fahrenheit p/ Kelvin \nE.Kelvin p/ Celcius \nF.Kelvin p/ Fahrenheit\n")
operacao = str(input("Quero realizar a converção de letra: "))
nu = float(input("Informe o valor que deseja converter: "))

def temperatura (nu,op):

  if op == "A":
    return (9/5 * nu) + 32
  elif op == "B":
    return nu + 273.15
  elif op == "C":
    return 5/9 * (nu - 32)
  elif op == "D":
    return (5/9) * (nu - 32) + 273.15
  elif op == "E":
    return nu - 273.15
  elif op == "F":
    return (9/5) * (nu - 273.15) + 32
  else:
    print("Operação inválida.")

resultado = (temperatura (nu, operacao))
print("Resultado:", resultado)