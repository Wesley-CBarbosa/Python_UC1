# Exercício 4: Verifique se um ano é bissexto.

ano = int(input("Informe o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ( ano % 400 == 0):
  print("Ano bissexto.")
else:
  print("Não é ano bissexto.")