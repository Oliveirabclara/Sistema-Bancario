menu = """
Bem vindo, digite uma opção: 
[d]: Depositar
[s]: Sacar
[e]: Extrato
[q]: Sair

=>"""
saldo = 0 
limite= 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3 

while True: 
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0: 
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n "
            print(f"Deposito realizado com sucesso no valor de {valor}")
        else:
            print("Opção falhou. O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente para essa transação. ")

        elif excedeu_limite:
            print("Operação falhou. O valor excedeu o limite para essa transação. ")

        elif excedeu_saques:
            print("Operação falhou. Você excedeu o limite de saques permitidos.")

        elif valor > 0: 
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saque += 1
            print(f"Saque realizado com sucesso no valor de {valor}")

        else: 
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "e":
        print("="*10 +"EXTRATO" + "="*10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo :.2f}")
        print("="*40)

    elif opcao == "q": 
        print("Foi um prazer tê-lo conosco hoje. Volte sempre.")
        break 

    else: 
        print("Opção inválida, tente novamente.")
