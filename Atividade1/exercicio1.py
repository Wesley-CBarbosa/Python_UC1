#Exercício 1: Verifique se um número é positivo, negativo ou zero.

def verifica_num(numero):
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("zero")

num = int(input("Digite um número: "))
verifica_num(num)