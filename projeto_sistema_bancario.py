menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """



def sistema_bancario():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:

        opcao = input(menu)

        if opcao == "1":
            
            valor_deposito = float(input("Informe o valor que deseja depositar: "))
            
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2F}\n"
                print(f"Valor depositado em sua conta: R$ {saldo:.2F}!")

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            
            valor_saque = float(input("Informe o valor que deseja sacar: "))

            if valor_saque > saldo: 
                print("Operação falhou! Não é possível fazer o saque por falta de saldo.")

            elif valor_saque > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            
            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Limite de saques excedido.")
            
            elif valor_saque > 0: 
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2F}\n"
                print(f"Valor do saque: R$ {valor_saque:.2F}")
                numero_saques += 1
            else:
                print("Operação falhou! O valor que foi informado é inválido.")
                
        elif opcao == "3":
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Sem movimentações na conta!")
            
            else:
                print(extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "0":
            print("Obrigado por usar o nosso sistema! Até a próxima.")
            break
        
        else:
            print("Operação inválida, por favor escolha uma das opções do menu")
            
sistema_bancario()