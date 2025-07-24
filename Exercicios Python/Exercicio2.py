#Exercício 2: Peça dois números e exiba o maior

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

def verifica_maior(num1, num2):
    if num1 > num2:
        print("O primeiro número é maior!")
    elif num1 == num2:
        print("Os valores são iguais!")
    else:
        print("O segundo número é maior!")

verifica_maior(n1, n2)