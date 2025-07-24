# Sistema Bancário

# saldo -= valor 
# saldo += valor 

# saldo1 -= valor
# saldo2 += valor 

# conta1 = '1234'
# saldo1 = 100.0

# conta2 = '7894'
# saldo2 = 2000.0

# while True:

#     print('Escolha um dos números referente as opções.')
#     print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')
#     op = int(input('Qual operação deseja realizar: '))

#     if op == 1:
#         print(f'O saldo da conta 1: {saldo1}')
#     elif op == 2:
#         valor = float(input('Escolha o valor do depósito: '))
#         saldo1 += valor 
#         print(f'O saldo atual da conta 1: {saldo1}')
#     elif op == 3:
#         saldo1 -= valor
#         saldo2 += valor
#         valor = float(input('Escolha o valor do transferencia: '))
#         print(f'O saldo atual da conta 1: {saldo1}')
#     elif op == 4:
#         valor = float(input('Escolha o valor do saque: '))
#         saldo1 -= valor 
#         print(f'O saldo atual da conta 1: {saldo1}')
#     elif op == 5:
#         print('Operação realizada! Agradecemos por seu tempo.')
#     break

# #-------------------------------------------------------------------------------------

# def exibir_menu():
#     print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')

# def sacar(valor):
#     global saldo
#     saldo -= valor 
#     print(f"O saldo atual da conta: {saldo}")

# def depositar(valor):
#     global saldo
#     saldo += valor 
#     print(f"O saldo atual da conta: {saldo}")

# def transferir(valor):
#     global saldo, destinatario
#     saldo -= valor 
#     destinatario += valor
#     print(f"O saldo atual da conta: {saldo}")


#-----------------------------------------------------------------------------------------------


# Criar um menu que permite ao usuário realizar N transferencias até que ele opte por sair.

while True:
  print("\nSeja bem vindo ao Banco Central")
  p = input('------------$------------ \nInforme o número da operação que deseja realizar. \n------------$------------ \n1-Consultar Saldo\n2-Saque\n3-Depósito\n4-Transferencia\n5-Sair\n -----------$------------\n ')
  saldo = 5000

  if p == '1':
      print(f'Seu saldo é de: R${saldo}')
  elif p == '2':
      print(f'\nO saldo atual da conta é de: {saldo}\n')
      valor = float(input('Informe o valor que deseja sacar: '))
      saldo -= valor 
      print(f'O novo saldo atual da conta é de: {saldo}')
  elif p == '3':
      deposito = float(input('Informe o valor que deseja depositar: R$ '))
      saldo += deposito
      print(f'Depósito realizado com sucesso! Seu saldo atual é de: R${saldo}')
  elif p == '4':
      transferencia = float(input('Informe o valor que deseja retirar: R$ '))
      saldo -= transferencia
      if saldo < 0:
          print('Saldo insuficiente.')
      else:
          print(f'Transferencia realizado com sucesso! Seu saldo atual é de: R${saldo}')
  elif p == '5':
      print('Você saiu do sistema. Até breve!')
      break