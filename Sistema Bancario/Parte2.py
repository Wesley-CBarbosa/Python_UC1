# Criar uma segunda conta corrente, para simular saque,depósito e transferência.

p = input('Informe o número da operação que deseja realizar?\n1-Saque\n2-Depósito\n3-Transferencia\n ')
saldo = 5000

if p == '1':
    print(f'\nO saldo atual da conta é de: {saldo}\n')
    valor = float(input('Informe o valor que deseja sacar: '))
    saldo -= valor 
    print(f'O novo saldo atual da conta é de: {saldo}')
elif p == '2':
    deposito = float(input('Informe o valor que deseja depositar: R$ '))
    saldo += deposito
    print(f'Depósito realizado com sucesso! Seu saldo atual é de: R${saldo}')
elif p == '3':
    transferencia = float(input('Informe o valor que deseja retirar: R$ '))
    saldo -= transferencia
    if saldo < 0:
        print('Saldo insuficiente.')
    else:
        print(f'Transferencia realizado com sucesso! Seu saldo atual é de: R${saldo}')
