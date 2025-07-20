# Exercício 14: Crie um menu onde o usuário pode escolher entre exibir a data, hora ou sair.

print("Informe que tipo de informação deseja exibir digitando a primeira letra da palavra.")
print("\nD.data \nH.hora \nS.sair\n")
operacao = str(input("Informe qual operação deseja realizar: "))

def menu (op):

  if op == "D":
    print("07/07/2025")
  elif op == "H":
    print("21:45")
  elif op == "S":
    print("Programa encerrado")
  else:
    print("O valor informado não se enquadra na condição proposta.")

resultado = (menu (operacao))