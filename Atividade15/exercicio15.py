# Exercício 15: Implemente um programa que identifica o dia da semana baseado em um número (1 = Segunda, 7 = Domingo).

print("Informe um número de 1 à 7 e descubra qual dia da semana é.")
operacao = int(input("\nInforme um valor: \n"))

def semana (op):

  if op == 1:
    print("Segunda")
  elif op == 2:
    print("Terça")
  elif op == 3:
    print("Quarta")
  elif op == 4:
    print("Quinta")
  elif op == 5:
    print("Sexta")
  elif op == 6:
    print("Sábado")
  elif op == 5:
    print("Domingo")
  else:
    print("O valor informado não se enquadra na condição proposta.")

resultado = (semana (operacao))