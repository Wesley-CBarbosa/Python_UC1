# Exercício 7: Verifique se já posso ir embora da aula de Análise de Dados sem assinar a folha.

print("\nUtilize este formato 00.00 para responder o  horário\n")
saida = float(input("Que horas são: "))


if saida >= 21.45:
  print("Pode ir embora.")
else:
  print("Ainda não está no horário, portanto não pode ir embora.")