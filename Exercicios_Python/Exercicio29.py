# Exercício 29: Imprima todas as vogais de uma string digitada pelo usuário.

texto = str(input("Digite uma palavra para ver somete as vogais dela: "))

vogais = 'aeiouAEIOU'

for letra in texto:
  if letra in vogais:
    print(letra)